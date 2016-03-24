# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0004_product_average_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.FloatField(null=True)),
                ('total_price', models.FloatField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='average_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(to='gestao.Product'),
        ),
    ]
