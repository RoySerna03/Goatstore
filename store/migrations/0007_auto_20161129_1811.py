# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_beyer',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='product',
            name='pruct_active',
            field=models.BooleanField(default=True),
        ),
    ]
