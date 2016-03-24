# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0010_auto_20160304_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(default=1, to='gestao.Product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='total_price',
            field=models.FloatField(default=123),
            preserve_default=False,
        ),
    ]
