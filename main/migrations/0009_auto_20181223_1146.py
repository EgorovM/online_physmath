# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-23 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20181223_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='photo',
            field=models.ImageField(default='images/default.jpg', upload_to='media/images'),
        ),
    ]
