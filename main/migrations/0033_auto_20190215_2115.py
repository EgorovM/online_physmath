# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-15 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20190215_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='color',
            field=models.CharField(blank=True, choices=[('#33691e', 'Зеленый'), ('#f44336', 'Красный'), ('#cddc39', 'Лаймовый'), ('#ff9800', 'Оранжевый'), ('#2196f3', 'Синий')], max_length=20),
        ),
    ]