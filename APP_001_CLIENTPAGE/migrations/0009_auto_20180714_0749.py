# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-14 07:49
from __future__ import unicode_literals

import APP_001_CLIENTPAGE.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP_001_CLIENTPAGE', '0008_remove_act_act_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actimage_name', models.CharField(max_length=120)),
                ('actimage_image', models.ImageField(upload_to=APP_001_CLIENTPAGE.models.upload_location)),
                ('actimage_act', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='act_images', to='APP_001_CLIENTPAGE.Act')),
            ],
        ),
        migrations.AlterField(
            model_name='praticien',
            name='praticien_phone_number',
            field=models.CharField(help_text='Exemple : 0608767898', max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be like 06XXXXXXXX', regex='^0\\d{9}$')]),
        ),
        migrations.AlterField(
            model_name='praticien',
            name='praticien_url_rdv',
            field=models.URLField(blank=True, help_text='Lien vers Doctolib par exemple', max_length=300, null=True),
        ),
    ]
