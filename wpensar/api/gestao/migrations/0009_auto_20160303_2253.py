# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0008_purchase_chart_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='chart_uuid',
            new_name='cart_uuid',
        ),
    ]
