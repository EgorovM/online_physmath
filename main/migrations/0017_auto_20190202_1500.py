# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-02 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20190202_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='arrive_time',
            field=models.TimeField(null=True, verbose_name='time arrive'),
        ),
    ]
