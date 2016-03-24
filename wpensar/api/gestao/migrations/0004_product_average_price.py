# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0003_auto_20160302_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='average_price',
            field=models.IntegerField(null=True),
        ),
    ]
