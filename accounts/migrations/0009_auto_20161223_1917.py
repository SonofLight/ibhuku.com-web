# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 00:17
from __future__ import unicode_literals

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20161223_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='expire_date',
            field=models.DateTimeField(default=accounts.models.get_account_valid_link_expire, verbose_name='expire date'),
        ),
    ]
