# -*- encoding: utf-8 -*-
from django import template
from bank.models import Account, Transaction

register = template.Library()

def group_required(user, *group_names):
	return bool(user.groups.filter(name__in=group_names))

def get_transaction_operation(transaction):
	return Transaction.OPERATIONS[transaction.operation][1]

register.simple_tag(group_required, name='group_required')
register.simple_tag(get_transaction_operation, name='get_transaction_operation')