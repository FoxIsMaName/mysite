# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManMon', '0005_auto_20170218_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='pub_time',
        ),
        migrations.AlterField(
            model_name='income',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
