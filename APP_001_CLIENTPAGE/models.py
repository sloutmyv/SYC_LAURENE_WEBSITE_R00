from django.core.validators import RegexValidator
from django.db import models

class Praticien(models.Model):
    praticien_first_name         = models.CharField(max_length=120)
    praticien_last_name          = models.CharField(max_length=120)
    phone_regex                  = RegexValidator(regex=r'^0\d{9}$', message='Phone number must be like 06XXXXXXXX')
    praticien_phone_number       = models.CharField(validators=[phone_regex], max_length=10)
    praticien_url_rdv            = models.URLField(max_length=300, null=True, blank=True)
    praticien_email              = models.EmailField(max_length=254)
    praticien_job                = models.CharField(max_length=120)
    praticien_image              = models.ImageField(null=True,blank=True)
    praticien_introduction       = models.TextField(null=True,blank=True)
    praticien_formation          = models.TextField(null=True,blank=True)
    praticien_experiences_pro    = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.praticien_first_name + ' ' + self.praticien_last_name

    def printable_number(self):
        number = self.praticien_phone_number
        txt=""
        for i in range(len(number)):
            txt += number[i]
            if i%2 == 1 and i < len(number)-1:
                txt += '.'
        return txt

class Office(models.Model):
    office_name         = models.CharField(max_length=120)
    office_adresse      = models.CharField(max_length=300)
    office_acces        = models.TextField(null=True,blank=True)
    office_description  = models.TextField(null=True,blank=True)
    office_image        = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.office_name
