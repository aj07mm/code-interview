# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum


from django.contrib.auth.models import User, Group
from models import Account, Transaction, Client
from forms import AccountTransactionForm, AccountCreateForm, ClientRegistrationForm
from registration.users import UserModel, UsernameField

from registration.views import RegistrationView
from django.db import models
from django.contrib.auth import load_backend, login

from django.views.generic.edit import FormView
from helpers import login_user

class ClientRegistration(RegistrationView):
	success_url = '/'
	form_class = ClientRegistrationForm

	def register(self, form):
		"""
		Implement user-registration logic here.

		"""
		User = UserModel()
		user = User.objects.create_user(
			username = form.cleaned_data['username'],
			first_name = form.cleaned_data['first_name'],
			last_name = form.cleaned_data['last_name'],
			email=form.cleaned_data['email'],
			password=form.cleaned_data['password1']
		)
		user.groups.add(Group.objects.get(name='account_holder'))
		Client.objects.create(
			user=user,
			cpf = form.cleaned_data['cpf'],
			created_at  = models.DateTimeField(auto_now_add=True)
		)
		login_user(self.request, user)

def index(request):
    return render(request, 'base.html', {})

# ACCOUNT

@login_required
def account_deposit(request, id=None):
	instance = get_object_or_404(Account, id=id)
	form = AccountTransactionForm(request.POST or None)
	if form.is_valid():
		instance.deposit(form.cleaned_data['amount'])
		messages.success(request, "Deposited!", extra_tags="html_safe")
		return HttpResponseRedirect('/account')

	context = {
		"title" : "Deposit",
		"instance" : instance,
		"form" : form
	}
	return render(request, 'account_deposit.html', context)

@login_required
def account_withdraw(request, id=None):
	instance = get_object_or_404(Account, id=id)
	form = AccountTransactionForm(request.POST or None)
	if form.is_valid():
		instance.withdraw(form.cleaned_data['amount'])
		messages.success(request, "Withdrawed!", extra_tags="html_safe")
		return HttpResponseRedirect('/account')
	context = {
		"title" : "Withdraw",
		"instance" : instance,
		"form" : form
	}
	return render(request, 'account_withdraw.html', context)

@login_required
def account_create(request):
	form = AccountCreateForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.client = request.user.client
		instance.save()
		messages.success(request, "Account created!", extra_tags="html_safe")
		return HttpResponseRedirect('/account')
	context = {
		"title" : "Create",
		"form" : form
	}
	return render(request, 'account_create.html', context)

@login_required
def account_list(request):
	queryset_list = Account.objects.filter(client = request.user.client).order_by("-id")
	paginator = Paginator(queryset_list, 4) # Show 25 queryset per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"accounts" : queryset,
		"title" : "Accounts",
		"total_balance" : Account.get_total_balance(request.user.client)
	}
	return render(request, 'account.html', context)

# REPORT

@login_required
def report_list(request):
	context = {
		"title" : "Reports"
	}
	return render(request, 'report.html', context)

@login_required
def report_balance(request):
	queryset_list = Account.objects.all().order_by("-id")

	paginator = Paginator(queryset_list, 10) # Show 25 queryset per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"accounts" : queryset,
		"title" : "Report Balance"
	}
	return render(request, 'report_balance.html', context)

@login_required
def report_transaction(request):
	queryset_list = Transaction.objects.all().order_by("-id")
	
	paginator = Paginator(queryset_list, 10) # Show 25 queryset per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"transactions" : queryset,
		"title" : "Report transaction"
	}
	return render(request, 'report_transaction.html', context)

@login_required
def report_transaction_operation(request, operation=None):
	if operation == None:
		return Http404

	queryset_list = Transaction.objects.filter(operation=Transaction.OPERATIONS_DICT[operation]).extra(select={'day': 'date( created_at )'}).values('day').annotate(total=Sum('amount'))

	paginator = Paginator(queryset_list, 10) # Show 25 queryset per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"transactions" : queryset,
		"title" : "Report transaction: " + operation
	}
	return render(request, 'report_transaction_operation.html', context)

@login_required
def account_detail(request, id=id):
	instance = get_object_or_404(Account, id=id)
	context = {
		"title" : "Detail",
		"instance" : instance
	}
	return render(request, 'account_detail.html', context)


#client

@login_required
def client_create(request):
	form = ClientForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Welcome to Orama Bank!", extra_tags="html_safe")
		return HttpResponseRedirect('/')
	context = {
		"title" : "Almost there",
		"form" : form
	}
	return render(request, 'client_create.html', context)