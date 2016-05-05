# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models

from django.db.models import Count, Sum
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save

## -- User subclasses -- ##

class Client(models.Model):
  user = models.OneToOneField(User)
  cpf = models.CharField(max_length=60)
  created_at = models.DateTimeField(auto_now_add=True)

class Manager(models.Model):
  user = models.OneToOneField(User)
  created_at = models.DateTimeField(auto_now_add=True)

## -- Other Entities -- ##

class Account(models.Model):
    balance = models.FloatField(default=0)
    client = models.ForeignKey(Client, blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def deposit(self, amount):
    	self.balance += amount;
        transaction = Transaction.objects.create(
            amount=amount,
            operation=Transaction.OPERATIONS_DICT['deposit'],
            account=self,
            created_at=models.DateTimeField(auto_now_add=True)
        )
        self.save()
    	return self.balance

    def withdraw(self, amount):
    	self.balance -= amount;
    	transaction = Transaction.objects.create(
    		amount=amount,
    		operation=Transaction.OPERATIONS_DICT['withdraw'],
    		account=self,
    		created_at=models.DateTimeField(auto_now_add=True)
    	)
        self.save()
    	return self.balance

    @staticmethod
    def get_total_balance(client):
        return Account.objects.filter(client=client).aggregate(total=Sum('balance'))['total']

    def get_absolute_url(self):
    	return reverse('account:detail', kwargs={"id" : self.id})

class Transaction(models.Model):
    OPERATIONS_DICT = {
        'deposit' : 0,
        'withdraw' : 1
    }
    OPERATIONS = (
        (OPERATIONS_DICT['deposit'], 'deposit'),
        (OPERATIONS_DICT['withdraw'], 'withdraw')
    )
    account = models.ForeignKey(Account, blank=True, null=True)
    amount   = models.FloatField(default=0)
    operation = models.IntegerField(choices=OPERATIONS)
    created_at  =  models.DateTimeField(auto_now_add=True)

# --- Signals ---

# def default_group(sender, instance, created, **kwargs):
#     if created:
#         instance.groups.add(Group.objects.get(name='account_holder'))

# def default_first_name(sender, instance, created, **kwargs):
#     if created:
#         instance.user.first_name = instance.

# post_save.connect(default_group, sender=User)
# post_save.connect(default_group, sender=Client)