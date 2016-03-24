# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0007_auto_20160303_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='chart_uuid',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
