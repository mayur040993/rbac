# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-14 16:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybarcapp', '0004_auto_20200314_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
    ]
