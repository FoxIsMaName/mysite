# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ManMon', '0011_auto_20170219_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='type_income',
            field=models.CharField(default='salary', max_length=200),
        ),
        migrations.AlterField(
            model_name='payment',
            name='type_payment',
            field=models.CharField(default='food', max_length=200),
        ),
        migrations.AlterField(
            model_name='typeincome',
            name='income',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ManMon.Income'),
        ),
        migrations.AlterField(
            model_name='typepayment',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ManMon.Payment'),
        ),
    ]
