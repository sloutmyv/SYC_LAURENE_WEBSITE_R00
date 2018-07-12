from django.contrib import admin
from django.db import models

from pagedown.widgets import AdminPagedownWidget

from .models import Praticien, Office, ActCategory

class PraticienAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(Praticien, PraticienAdmin)

class OfficeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(Office, OfficeAdmin)

class ActCategoryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(ActCategory, ActCategoryAdmin)
