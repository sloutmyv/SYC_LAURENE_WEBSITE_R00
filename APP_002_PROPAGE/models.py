from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save

from APP_001_CLIENTPAGE.utils import unique_slug_generator

class Patient(models.Model):
    patient_first_name         = models.CharField(max_length=120,verbose_name="Prénom")
    patient_last_name          = models.CharField(max_length=120,verbose_name="Nom")
    patient_maiden_name        = models.CharField(max_length=120,verbose_name="Nom de jeune fille", null=True, blank=True)
    patient_birthday           = models.DateTimeField(null=True,blank=True)

    phone_regex                = RegexValidator(regex=r'^0\d{9}$', message='Phone number must be like 06XXXXXXXX')
    patient_phone_number       = models.CharField(validators=[phone_regex], max_length=10, verbose_name="Téléphone")

    # Adresse
    patient_address            = models.CharField(max_length=300, verbose_name="Adresse", null=True, blank=True)
    patient_zip_code           = models.CharField(max_length=5, verbose_name="Code postal", null=True, blank=True)
    patient_city               = models.CharField(max_length=64, verbose_name="Ville", null=True, blank=True)
    patient_contry             = models.CharField(max_length=64, default="France", verbose_name="Pays",null=True, blank=True)

    SITUATIONS                 = (
                                  ("celibataire","Célibataire"),
                                  ("en_couple","En couple"),
                                  ("mariee","Mariée")
                                  )
    patient_situation          = models.CharField(max_length=100,choices=SITUATIONS, default="celibataire", verbose_name="Situation familiale",null=True, blank=True)
    patient_job                = models.CharField(max_length=120,verbose_name="Profession", null=True, blank=True)
    patient_gyn                = models.CharField(max_length=200,verbose_name="Gynécologue", null=True, blank=True)
    patient_med                = models.CharField(max_length=200,verbose_name="Médecin traitant", null=True, blank=True)

    patient_taille             = models.FloatField(verbose_name="Taille (m)",null=True, blank=True)
    patient_poid               = models.IntegerField(verbose_name="Poids (Kg)", null=True, blank=True)

    patient_ant_fam            = models.TextField(verbose_name="Antécédants familiaux", null=True, blank=True)
    patient_ant_perso          = models.TextField(verbose_name="Antécédants personnels", null=True, blank=True)
    patient_ant_chir           = models.TextField(verbose_name="Antécédants chirurgicaux", null=True, blank=True)
    patient_ant_gyn            = models.TextField(verbose_name="Antécédants gynécologiques", null=True, blank=True)


    CONTRACEPTIONS             = (
                                  ("rien","Pas de contraception"),
                                  ("anneau_vaginal","Anneau vignal"),
                                  ("DIU","DIU"),
                                  ("implant","Implant contraceptif"),
                                  ("ligature","Ligature des trompes"),
                                  ("obturation","Obturation des trompes"),
                                  ("patch","Patch"),
                                  ("pilule","Pilule contraceptive"),
                                  ("progestatif_en_injection","Progestatifs en injections"),
                                  )
    patient_contraception      = models.CharField(max_length=100,choices=CONTRACEPTIONS,default="rien",verbose_name="Contraception",null=True, blank=True)
    patient_FCV_bool           = models.BooleanField(default=False, verbose_name="FCV", blank=True)
    patient_FCV_com            = models.CharField(max_length=300, verbose_name="FCV informations", null=True, blank=True)
    patient_addictions         = models.CharField(max_length=300, verbose_name="Tabac/addications", null=True, blank=True)
    patient_allergies          = models.CharField(max_length=300, verbose_name="Allergie(s)", null=True, blank=True)

    slug                       = models.SlugField(null=True, blank=True)
    created_at                 = models.DateTimeField(auto_now_add=True)
    updated_at                 = models.DateTimeField(auto_now=True)


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

    def get_imc(self):
        return self.patient_poid / (self.patient_taille*self.patient_taille)

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
