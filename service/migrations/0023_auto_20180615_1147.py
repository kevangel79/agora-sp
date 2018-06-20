# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-15 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0022_merge_20180601_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceadminship',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serviceadminship',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
