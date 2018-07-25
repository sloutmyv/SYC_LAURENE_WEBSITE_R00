# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-25 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('APP_002_PROPAGE', '0016_auto_20180725_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patient_birthday',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
