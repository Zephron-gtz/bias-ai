# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20180411_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='site',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
