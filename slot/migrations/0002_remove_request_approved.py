# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-01 05:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='approved',
        ),
    ]