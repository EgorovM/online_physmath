# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-12 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20190206_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='status',
            field=models.CharField(choices=[('absent', '\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442'), ('present', '\u041f\u0440\u0438\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442'), ('leave', '\u0412\u044b\u0448\u0435\u043b \u0438\u0437 \u0448\u043a\u043e\u043b\u044b'), ('ill', '\u0411\u043e\u043b\u0435\u0435\u0442'), ('reason', '\u0423\u0432\u0430\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u0438\u0447\u0438\u043d\u0430')], default='absent', max_length=50),
        ),
    ]
