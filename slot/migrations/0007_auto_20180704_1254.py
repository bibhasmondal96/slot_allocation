# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-04 07:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slot', '0006_auto_20180704_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='client',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='freelancer',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='freelancer',
            name='longitude',
        ),
    ]