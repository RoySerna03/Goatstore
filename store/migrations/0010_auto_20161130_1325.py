# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 13:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0009_auto_20161129_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money_amount', models.PositiveIntegerField()),
                ('money_request_active', models.BooleanField(default=True)),
                ('money_requester_email', models.EmailField(max_length=254)),
                ('money_requester', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='balance',
            field=models.PositiveIntegerField(default=1000),
        ),
    ]
