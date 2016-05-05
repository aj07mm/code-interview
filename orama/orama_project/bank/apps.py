# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save

from django.apps import AppConfig

class BankConfig(AppConfig):
    name = 'bank'