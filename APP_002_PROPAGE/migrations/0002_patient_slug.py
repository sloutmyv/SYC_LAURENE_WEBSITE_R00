# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-15 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_002_PROPAGE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
    ]