# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-01 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slot', '0002_remove_request_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='status',
            field=models.CharField(choices=[('1', 'APPROVED'), ('0', 'CANCELED'), ('2', 'COMPLETED')], default='2', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('1', 'APPROVED'), ('0', 'REJECTED'), ('2', 'WAITING')], default='1', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slot',
            name='status',
            field=models.CharField(choices=[('1', 'APPROVED'), ('0', 'REJECTED'), ('2', 'COMPLETED')], max_length=2),
        ),
    ]