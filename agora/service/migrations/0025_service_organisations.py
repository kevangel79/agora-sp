# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-21 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_user_organisations'),
        ('service', '0024_servicedetails_visible_to_marketplace'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='organisations',
            field=models.ManyToManyField(blank=True, to='accounts.Organisation'),
        ),
    ]
