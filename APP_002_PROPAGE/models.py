from django.core.validators import RegexValidator
from django.db import models

class Patient(models.Model):
    patient_first_name         = models.CharField(max_length=120)
    patient_last_name          = models.CharField(max_length=120)
    phone_regex                = RegexValidator(regex=r'^0\d{9}$', message='Phone number must be like 06XXXXXXXX')
    praticien_phone_number     = models.CharField(validators=[phone_regex], max_length=10, help_text='Exemple : 0608767898')

    class Meta:
        verbose_name = 'Patiente'
        verbose_name_plural = 'Patientes'

    def __str__(self):
        return self.patient_first_name + ' ' + self.patient_last_name
