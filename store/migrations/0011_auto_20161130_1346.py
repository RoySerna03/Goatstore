# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 13:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20161130_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneyrequest',
            name='money_requester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
