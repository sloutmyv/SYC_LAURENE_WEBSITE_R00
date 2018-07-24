# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-23 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_002_PROPAGE', '0005_auto_20180723_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='patient_adresse',
        ),
        migrations.AddField(
            model_name='patient',
            name='address_1',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='city',
            field=models.CharField(default='Corbas', max_length=64),
        ),
        migrations.AddField(
            model_name='patient',
            name='contry',
            field=models.CharField(default='France', max_length=64),
        ),
        migrations.AddField(
            model_name='patient',
            name='zip_code',
            field=models.CharField(default='69960', max_length=5),
        ),
        migrations.DeleteModel(
            name='Adress',
        ),
    ]
