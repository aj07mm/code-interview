# -*- encoding: utf-8 -*-
from django import forms
from models import Account, Client
from registration.forms import RegistrationForm
from registration.users import UserModel, UsernameField
from django.contrib.auth.admin import UserAdmin, User
from bank.form_fields import BRCPFCNPJField

class AccountTransactionForm(forms.Form):
	amount = forms.FloatField(min_value=0.0)
	class Meta:
		model = Account
		fields = [
			"amount"
		]

class AccountCreateForm(forms.ModelForm):
	balance = forms.FloatField(min_value=0.0)
	class Meta:
		model = Account
		fields = [
			"balance"
		]

class ClientRegistrationForm(RegistrationForm):
	## ----- User default fields ----- #
	username = forms.CharField(max_length=15, label='Username')
	first_name = forms.CharField(max_length=15, label='First name')
	last_name = forms.CharField(max_length=15, label='Last name')

	## ----- Client default fields ----- #
	cpf = BRCPFCNPJField()

	class Meta:
		model = UserModel()
		fields = (UsernameField(), "email", 'first_name', 'last_name', 'cpf')


## -- admin form --- ##


class ClientAdminForm(forms.ModelForm):
	cpf = BRCPFCNPJField()

	class Meta:
		model = Client()
		fields = ('user','cpf' ,)
