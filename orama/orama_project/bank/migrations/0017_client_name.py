# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 06:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0016_auto_20160326_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 3, 26, 6, 5, 14, 606199, tzinfo=utc), max_length=60),
            preserve_default=False,
        ),
    ]
