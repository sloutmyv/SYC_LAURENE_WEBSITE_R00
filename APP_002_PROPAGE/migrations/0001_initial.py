# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-14 17:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_first_name', models.CharField(max_length=120)),
                ('patient_last_name', models.CharField(max_length=120)),
                ('praticien_phone_number', models.CharField(help_text='Exemple : 0608767898', max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be like 06XXXXXXXX', regex='^0\\d{9}$')])),
            ],
            options={
                'verbose_name': 'Patiente',
                'verbose_name_plural': 'Patientes',
            },
        ),
    ]