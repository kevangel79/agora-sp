# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-07-20 13:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0091_auto_20200720_1305'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='serviceadminship',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='serviceadminship',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='serviceadminship',
            name='service',
        ),
        migrations.DeleteModel(
            name='ServiceAdminship',
        ),
    ]
