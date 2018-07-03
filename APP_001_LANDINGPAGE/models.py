from django.core.validators import RegexValidator
from django.db import models

class InfosProfessionnel(models.Model):
    first_name      = models.CharField(max_length=120)
    last_name       = models.CharField(max_length=120)
    job             = models.CharField(max_length=120)
    phone_regex     = RegexValidator(regex=r'^\+33\d{9}$', message='Phone number must be like +33XXXXXXXXX')
    phone_number    = models.CharField(validators=[phone_regex], max_length=12)
    email           = models.EmailField(max_length=254)
    pro_adress      = models.CharField(max_length=300)

    def __str__(self):
        return self.last_name
