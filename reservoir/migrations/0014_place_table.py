# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-28 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservoir', '0013_decoration'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='table',
            field=models.IntegerField(default=-1, verbose_name='Číslo stolu'),
        ),
    ]