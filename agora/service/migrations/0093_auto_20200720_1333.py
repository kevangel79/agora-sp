# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-07-20 13:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0092_auto_20200720_1329'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='servicedetails',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='servicedetails',
            name='access_policies',
        ),
        migrations.RemoveField(
            model_name='servicedetails',
            name='id_service',
        ),
        migrations.RemoveField(
            model_name='servicedetails',
            name='service_trl',
        ),
        migrations.RemoveField(
            model_name='servicedetails',
            name='status',
        ),
        migrations.DeleteModel(
            name='UserRole',
        ),
        migrations.DeleteModel(
            name='ServiceDetails',
        ),
    ]
