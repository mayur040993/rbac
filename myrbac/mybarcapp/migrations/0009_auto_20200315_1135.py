# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-15 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybarcapp', '0008_auto_20200314_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]