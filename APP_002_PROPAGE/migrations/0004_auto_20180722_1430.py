# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-22 14:30
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_002_PROPAGE', '0003_auto_20180715_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='praticien_phone_number',
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_phone_number',
            field=models.CharField(default=0, max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be like 06XXXXXXXX', regex='^0\\d{9}$')]),
            preserve_default=False,
        ),
    ]
