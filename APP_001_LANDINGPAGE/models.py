from django.core.validators import RegexValidator
from django.db import models

class InfosProfessionnelles(models.Model):
    first_name      = models.CharField(max_length=120)
    last_name       = models.CharField(max_length=120)
    job             = models.CharField(max_length=120)
    phone_regex     = RegexValidator(regex=r'^\+33\d{9}$', message='Phone number must be like +33XXXXXXXXX')
    phone_number    = models.CharField(validators=[phone_regex], max_length=12)
    phone_number_p  = models.CharField(max_length=120,blank=True, null=True, editable=False)
    email           = models.EmailField(max_length=254)
    pro_adress      = models.CharField(max_length=300)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def printable_number(self):
        number = self.phone_number
        return ''.join('0'+number[3:])

    def save(self, *args, **kwargs):
        if not self.phone_number_p:
            self.phone_number_p = self.printable_number()
        super(InfosProfessionnelles, self).save(*args, **kwargs)
