# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-31 12:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20190131_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='arrive_time',
            field=models.TimeField(default=datetime.time(12, 54, 35, 169900), verbose_name='time arrive'),
        ),
    ]
