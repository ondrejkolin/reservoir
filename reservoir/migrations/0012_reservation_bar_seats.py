# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-27 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservoir', '0011_auto_20171213_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='bar_seats',
            field=models.IntegerField(default=0, verbose_name='Místa bez čísla: '),
        ),
    ]