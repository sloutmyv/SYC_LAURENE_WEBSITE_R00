from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save

from APP_001_CLIENTPAGE.utils import unique_slug_generator


class Patient(models.Model):
    patient_first_name         = models.CharField(max_length=120)
    patient_last_name          = models.CharField(max_length=120)
    phone_regex                = RegexValidator(regex=r'^0\d{9}$', message='Phone number must be like 06XXXXXXXX')
    praticien_phone_number     = models.CharField(validators=[phone_regex], max_length=10, help_text='Exemple : 0608767898')
    slug                       = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = 'Patiente'
        verbose_name_plural = 'Patientes'

    def __str__(self):
        return self.patient_first_name + ' ' + self.patient_last_name

    @property
    def title(self):
        return self.patient_first_name + '-' + self.patient_last_name

    def get_absolute_url(self):
        return reverse("propage:patient-details", kwargs={'slug': self.slug})

# Signaux création slugs
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Patient)