# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 06:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0017_client_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 26, 6, 5, 24, 743664, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
