# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-11-09 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_auto_20190602_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='rate',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3),
        ),
    ]
