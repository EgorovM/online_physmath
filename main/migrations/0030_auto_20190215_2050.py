# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-15 11:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20190215_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Pupil'),
        ),
    ]
