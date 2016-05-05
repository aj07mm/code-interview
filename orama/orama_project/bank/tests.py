# -*- encoding: utf-8 -*-
from django.test import TestCase
from bank.models import Account, Transaction, Client, Manager
from django.db import models
from django.contrib.auth.models import User, Group
from bank.templatetags.helpers import group_required, get_transaction_operation

class AccountTestCase(TestCase):

    def setUp(self):
        account_holder = Group()
        account_holder.name = 'account_holder'
        account_holder.save()

        user = User.objects.create_user(
            username="foo",
            email="foo@bar.com",
            password="123123"
        )
        user.groups.add(Group.objects.get(name='account_holder'))

        client = Client.objects.create(
            user=user,
            cpf="foo@bar.com",
            created_at=models.DateTimeField(auto_now_add=True)
        )
        account = Account.objects.create(
        	balance=99999, 
        	client= client, 
        	created_at=models.DateTimeField(auto_now_add=True)
        )

    # ---- Models ---- #

    def test_accounts_deposit(self):
        account = Account.objects.get(id=1)
        self.assertEqual(account.deposit(1), 100000)

    def test_accounts_withdraw(self):
        account = Account.objects.get(id=1)
        self.assertEqual(account.withdraw(1), 99998)

    def test_accounts_get_total_balance(self):
        client = Client.objects.get(id=1)
        total_balance = Account.get_total_balance(client)
        self.assertEqual(total_balance, 99999)


    # ---- Helpers ---- #

    def test_helper_group_required(self):
        user = User.objects.get(id=1)
        self.assertEqual(group_required(user, 'account_holder'), True)

    def test_helper_get_transaction_operation_deposit(self):
        transaction = Transaction.objects.create(
            account = Account.objects.get(id=1),
            amount   = 99999,
            operation = Transaction.OPERATIONS_DICT['deposit'],
            created_at  =  models.DateTimeField(auto_now_add=True)
        )
        self.assertEqual(get_transaction_operation(transaction), 'deposit')

    def test_helper_get_transaction_operation_withdraw(self):
        transaction = Transaction.objects.create(
            account = Account.objects.get(id=1),
            amount   = 99999,
            operation = Transaction.OPERATIONS_DICT['withdraw'],
            created_at  =  models.DateTimeField(auto_now_add=True)
        )
        self.assertEqual(get_transaction_operation(transaction), 'withdraw')