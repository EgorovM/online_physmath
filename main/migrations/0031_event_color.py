# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-15 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20190215_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='color',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
