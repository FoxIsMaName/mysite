# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 13:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManMon', '0021_auto_20170226_0515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='pub_time',
        ),
    ]