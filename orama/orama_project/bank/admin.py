# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, User
from django.contrib.auth.models import User, Group
from registration.forms import RegistrationForm
from django.conf import settings
from models import Account, Transaction, Client, Manager
from bank.form_fields import BRCPFCNPJField
from bank.forms import ClientRegistrationForm, ClientAdminForm

from django.db import models

def get_model_field_names(ModelClass):
    return map(lambda x: x.name, ModelClass._meta.fields)

# Register your models here.

## -- User subclasses -- ##

class ClientAdmin(admin.ModelAdmin):
    list_display = get_model_field_names(Client)

    form = ClientAdminForm

    def save_model(self, request, obj, form, change):
        obj.user = form.cleaned_data['user']
        obj.user.groups.add(Group.objects.get(name='account_holder'))
        obj.save()

class ManagerAdmin(admin.ModelAdmin):
    list_display = get_model_field_names(Manager)

    def save_model(self, request, obj, form, change):
        obj.user = form.cleaned_data['user']
        obj.user.groups.add(Group.objects.get(name='account_manager'))
        obj.save()

## -- Other Entities -- ##

class AccountAdmin(admin.ModelAdmin):
    list_display = get_model_field_names(Account)

class TransactionAdmin(admin.ModelAdmin):
    list_display = get_model_field_names(Transaction)

admin.site.register(Client, ClientAdmin)
admin.site.register(Manager, ManagerAdmin)

admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)

# admin.site.unregister(User)
# admin.site.register(settings.AUTH_USER_MODEL, CustomUserAdmin)