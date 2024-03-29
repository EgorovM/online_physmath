# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-02 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_merge_20190202_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='grade',
            field=models.CharField(choices=[('11FM', '11 \u0444\u0438\u0437\u0438\u043a\u043e-\u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u043b\u0430\u0441\u0441'), ('11ENG', '11 \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u043d\u044b\u0439 \u043a\u043b\u0430\u0441\u0441'), ('11TECH', '11 \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u043b\u0430\u0441\u0441'), ('11PTH', '11 \u043f\u043e\u043b\u0438\u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u043b\u0430\u0441\u0441'), ('11BCH', '11 \u0431\u0438\u043e\u043b\u043e\u0433\u043e-\u0445\u0438\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u043b\u0430\u0441\u0441'), ('11HUM', '11 \u0433\u0443\u043c\u0430\u043d\u0438\u0442\u0430\u0440\u043d\u044b\u0439 \u043a\u043b\u0430\u0441\u0441'), ('10FM', '10 \u0444\u0438\u0437\u0438\u043a\u043e-\u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439'), ('10ENG', '10 \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u043d\u044b\u0439 \u043a\u043b\u0430\u0441\u0441'), ('10TECH', '10 \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u043b\u0430\u0441\u0441'), ('10PTH', '10 \u043f\u043e\u043b\u0438\u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u043b\u0430\u0441\u0441'), ('10BCH', '10 \u0431\u0438\u043e\u043b\u043e\u0433\u043e-\u0445\u0438\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u043b\u0430\u0441\u0441'), ('10HUM', '10 \u0433\u0443\u043c\u0430\u043d\u0438\u0442\u0430\u0440\u043d\u044b\u0439 \u043a\u043b\u0430\u0441\u0441'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='status',
            field=models.CharField(choices=[('absent', '\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442'), ('present', '\u041f\u0440\u0438\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442'), ('ill', '\u0411\u043e\u043b\u0435\u0435\u0442'), ('reason', '\u0423\u0432\u0430\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u0438\u0447\u0438\u043d\u0430')], default='absent', max_length=50),
        ),
    ]
