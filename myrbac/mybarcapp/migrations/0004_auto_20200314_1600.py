# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-14 16:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybarcapp', '0003_auto_20200314_1600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='users_Role',
            new_name='users',
        ),
    ]