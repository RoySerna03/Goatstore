# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20161128_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.TextField(default=111),
            preserve_default=False,
        ),
    ]
