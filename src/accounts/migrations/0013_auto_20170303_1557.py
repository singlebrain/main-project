# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(default=b'user.png', upload_to=b''),
        ),
    ]