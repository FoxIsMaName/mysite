# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManMon', '0002_auto_20170215_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='pub_time',
            field=models.TimeField(auto_now=True),
        ),
    ]
