# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-23 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181223_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='pupil',
            name='photo',
            field=models.ImageField(default='images/default.jpg', upload_to='images'),
        ),
    ]
