# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_cost',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_qty',
            field=models.PositiveIntegerField(),
        ),
    ]