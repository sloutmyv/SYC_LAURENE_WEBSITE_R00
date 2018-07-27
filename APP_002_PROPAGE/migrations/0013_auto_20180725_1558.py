# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-25 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_002_PROPAGE', '0012_patient_patient_situation'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patient_gyn',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Gynécologue'),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_job',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Profession'),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_med',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Médecin traitant'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_address',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Adresse'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_city',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Ville'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_contry',
            field=models.CharField(blank=True, default='France', max_length=64, null=True, verbose_name='Pays'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_situation',
            field=models.CharField(blank=True, choices=[('celibataire', 'Célibataire'), ('en_couple', 'En couple'), ('mariee', 'Mariée')], default='celibataire', max_length=100, null=True, verbose_name='Situation familiale'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_zip_code',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Code postal'),
        ),
    ]