# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20161223_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='last login'),
        ),
    ]
