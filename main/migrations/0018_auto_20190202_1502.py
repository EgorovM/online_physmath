# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-02 06:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20190202_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='arrive_time',
            field=models.TimeField(default=datetime.datetime(2019, 2, 2, 6, 2, 52, 67539, tzinfo=utc), null=True, verbose_name='time arrive'),
        ),
    ]
