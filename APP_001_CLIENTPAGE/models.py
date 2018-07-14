from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_slug_generator

def upload_location(instance, filename):
    return '%s/%s/%s.jpg' % (instance._meta.verbose_name,instance.id, instance.slug)


class Praticien(models.Model):
    praticien_first_name         = models.CharField(max_length=120)
    praticien_last_name          = models.CharField(max_length=120)
    phone_regex                  = RegexValidator(regex=r'^0\d{9}$', message='Phone number must be like 06XXXXXXXX')
    praticien_phone_number       = models.CharField(validators=[phone_regex], max_length=10, help_text='Exemple : 0608767898')
    praticien_url_rdv            = models.URLField(max_length=300, null=True, blank=True, help_text='Lien vers Doctolib par exemple')
    praticien_email              = models.EmailField(max_length=254)
    praticien_job                = models.CharField(max_length=120)
    praticien_image              = models.ImageField(upload_to=upload_location, null=True,blank=True)
    praticien_introduction       = models.TextField(null=True,blank=True)
    praticien_formation          = models.TextField(null=True,blank=True)
    praticien_experiences_pro    = models.TextField(null=True,blank=True)
    slug                         = models.SlugField(null=True, blank=True, editable=False)

    class Meta:
        verbose_name = 'Le praticien'
        verbose_name_plural = 'Le praticien'

    def __str__(self):
        return self.praticien_first_name + ' ' + self.praticien_last_name

    @property
    def title(self):
        return self.praticien_first_name + '_' + self.praticien_last_name

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

    class Meta:
        verbose_name = 'Le cabinet'
        verbose_name_plural = 'Le cabinet'

    def __str__(self):
        return self.office_name

class ActCategory(models.Model):
    actcategory_name                = models.CharField(max_length=120)
    actcategory_short_description   = models.TextField(null=True,blank=True)
    actcategory_long_description    = models.TextField(null=True,blank=True)
    actcategory_image               = models.ImageField(upload_to=upload_location,null=True, blank=True)
    slug                            = models.SlugField(null=True, blank=True, editable=False)

    class Meta:
        verbose_name = 'Act category'
        verbose_name_plural = 'Acts categories'

    def __str__(self):
        return self.actcategory_name

    @property
    def title(self):
        return self.actcategory_name

class Act(models.Model):
    act_category    = models.ForeignKey(ActCategory, related_name='acte')
    act_name_small  = models.CharField(max_length=120, help_text='Texte de la barre de navigation')
    act_name_long   = models.CharField(max_length=120, help_text="Titre de l'article")
    act_description = models.TextField(null=True,blank=True)
    slug            = models.SlugField(null=True, blank=True,editable=False)

    class Meta:
        verbose_name = 'Act'
        verbose_name_plural = 'Acts'

    def __str__(self):
        return self.act_name_small

    @property
    def title(self):
        return self.act_name_small

class ActImage(models.Model):
    actimage_act   = models.ForeignKey(Act, related_name='act_images')
    actimage_name  = models.CharField(max_length=120)
    actimage_image = models.ImageField(upload_to=upload_location,null=True, blank=True)
    slug           = models.SlugField(null=True, blank=True, editable=False)

    @property
    def title(self):
        return self.actimage_name




# Signaux création slugs
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=ActCategory)
pre_save.connect(rl_pre_save_receiver, sender=Act)
pre_save.connect(rl_pre_save_receiver, sender=ActImage)
pre_save.connect(rl_pre_save_receiver, sender=Praticien)
