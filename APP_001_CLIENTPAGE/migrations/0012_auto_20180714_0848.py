# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-14 08:48
from __future__ import unicode_literals

import APP_001_CLIENTPAGE.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_001_CLIENTPAGE', '0011_auto_20180714_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actcategory',
            name='actcategory_image',
            field=models.ImageField(blank=True, null=True, upload_to=APP_001_CLIENTPAGE.models.upload_location),
        ),
    ]
