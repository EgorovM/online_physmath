# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-31 12:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20190131_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='arrive_time',
            field=models.TimeField(default=datetime.time(21, 58, 11, 675037), verbose_name='time arrive'),
        ),
    ]
