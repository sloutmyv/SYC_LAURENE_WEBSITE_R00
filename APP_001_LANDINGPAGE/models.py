from django.core.validators import RegexValidator
from django.db import models

class Description(models.Model):
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
        super(Description, self).save(*args, **kwargs)

def upload_location(instance, filename):
    return '%s/%s' % (instance.id, filename)

class ActCategory(models.Model):
    category            = models.CharField(max_length=120)
    description         = models.TextField()
    image_carousel      = models.ImageField(upload_to=upload_location,
                                        null=True,
                                        blank=True,
                                        width_field="width_field",
                                        height_field="height_field")
    width_field     = models.IntegerField(default=0)
    height_field    = models.IntegerField(default=0)

    def __str__(self):
        return self.category

    def save(self, *args, **kwargs):
        for field_name in ['categorie']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.upper())
        super(ActCategory, self).save(*args, **kwargs)

class Act(models.Model):
    act_category        = models.ForeignKey(ActCategory, related_name='act_category')
    act                 = models.CharField(max_length=120)
    act_description     = models.TextField()
    act_image           = models.ImageField(upload_to=upload_location,
                                                null=True,
                                                blank=True,
                                                width_field="width_field",
                                                height_field="height_field")
    width_field      = models.IntegerField(default=0)
    height_field     = models.IntegerField(default=0)

    def __str__(self):
        return self.act
