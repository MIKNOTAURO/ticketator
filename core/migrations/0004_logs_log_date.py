# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-23 18:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_microtasks_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='log_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
