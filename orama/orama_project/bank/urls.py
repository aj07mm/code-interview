# -*- encoding: utf-8 -*-
from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.index, name='/'),
	#account
	url(r'^account/$', views.account_list, name='account_list'),
	url(r'^account/create/$', views.account_create, name='account_create'),
    url(r'^account/(?P<id>\d+)/detail/$', views.account_detail, name='account_detail'), #id or pk
    url(r'^account/(?P<id>\d+)/deposit/$', views.account_deposit, name='account_deposit'), #id or pk
    url(r'^account/(?P<id>\d+)/withdraw/$', views.account_withdraw, name='account_withdraw'),
	#report
	url(r'^report/$', views.report_list, name='report_list'),
	url(r'^report/account/balance/$', views.report_balance, name='report_balance'),
	url(r'^report/account/transaction/$', views.report_transaction, name='report_transaction'),
	url(r'^report/account/transaction/(?P<operation>\w+)/$', views.report_transaction_operation, name='report_transaction_operation'),
]