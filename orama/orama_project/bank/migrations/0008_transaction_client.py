# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0007_auto_20160325_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bank.Client'),
        ),
    ]
