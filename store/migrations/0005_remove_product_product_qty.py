# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 23:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_qty',
        ),
    ]
