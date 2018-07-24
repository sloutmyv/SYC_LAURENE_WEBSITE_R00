from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save

from APP_001_CLIENTPAGE.utils import unique_slug_generator

class Patient(models.Model):
    patient_first_name         = models.CharField(max_length=120,verbose_name="Prénom")
    patient_last_name          = models.CharField(max_length=120,verbose_name="Nom")
    phone_regex                = RegexValidator(regex=r'^0\d{9}$', message='Phone number must be like 06XXXXXXXX')
    patient_phone_number       = models.CharField(validators=[phone_regex], max_length=10, verbose_name="Téléphone")
    slug                       = models.SlugField(null=True, blank=True)
    patient_address            = models.CharField(max_length=300, verbose_name="Adresse")
    patient_zip_code           = models.CharField(max_length=5, default="69960", verbose_name="Code postal")
    patient_city               = models.CharField(max_length=64, default="Corbas", verbose_name="Ville")
    patient_contry             = models.CharField(max_length=64, default="France", verbose_name="Pays")
    created_at                 = models.DateTimeField(auto_now_add=True)
    updated_at                 = models.DateTimeField(auto_now=True)
    patient_note               = models.TextField(null=True, blank=True, default="Pas de remarques")

    class Meta:
        verbose_name = 'Patiente'
        verbose_name_plural = 'Patientes'

    def __str__(self):
        return self.patient_first_name + ' ' + self.patient_last_name

    def call_number(self):
        number = self.patient_phone_number
        return number[1:]

    def get_absolute_url(self):
        return reverse("propage:patient-details", kwargs={'slug': self.slug})

    def get_adress(self):
        return self.patient_address + ", " + self.patient_zip_code + " " + self.patient_city + " - " + self.patient_contry

    def printable_number(self):
        number = self.patient_phone_number
        txt=""
        for i in range(len(number)):
            txt += number[i]
            if i%2 == 1 and i < len(number)-1:
                txt += '.'
        return txt

    @property
    def title(self):
        return self.patient_first_name + '-' + self.patient_last_name

# Signaux création slugs
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Patient)
