# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0007_auto_20170307_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apt_test',
            name='time',
            field=models.DurationField(default='1:00:00'),
        ),
    ]