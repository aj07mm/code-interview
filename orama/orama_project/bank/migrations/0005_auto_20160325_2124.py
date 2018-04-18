# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 21:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_client_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='category',
        ),
        migrations.AddField(
            model_name='transaction',
            name='operation',
            field=models.CharField(choices=[('Deposit', 'Deposit'), ('Withdraw', 'Withdraw')], default=datetime.datetime(2016, 3, 25, 21, 24, 37, 416445, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]