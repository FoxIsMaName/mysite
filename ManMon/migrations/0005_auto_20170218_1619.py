# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManMon', '0004_auto_20170218_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='pub_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='pub_date',
            field=models.DateField(auto_now=True),
        ),
    ]
