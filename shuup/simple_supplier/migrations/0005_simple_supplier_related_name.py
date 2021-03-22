# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-14 16:55
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_supplier', '0004_stockadjustment_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockcount',
            name='product',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='simple_supplier_stock_count', to='shuup.Product', verbose_name='product'),
        ),
    ]
