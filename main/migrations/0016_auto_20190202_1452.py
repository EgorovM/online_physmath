# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-02 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20190202_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='arrive_time',
            field=models.TimeField(blank=True, verbose_name='time arrive'),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='grade',
            field=models.CharField(choices=[('11 физико-математический', '11FM'), ('11 инженерный класс', '11ENG'), ('11 технический класс', '11TECH'), ('11 политехнический класс', '11PTH'), ('11 биолого-химический класс', '11BCH'), ('11 гуманитарный класс', '11HUM'), ('10 физико-математический', '10FM'), ('10 инженерный класс', '10ENG'), ('10 технический класс', '10TECH'), ('10 политехнический класс', '10PTH'), ('10 биолого-химический класс', '10BCH'), ('10 гуманитарный класс', '10HUM'), ('9 класс', '9'), ('8 класс', '8'), ('7 класс', '7'), ('6 класс', '6'), ('5 класс', '5')], max_length=50),
        ),
    ]
