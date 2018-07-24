# Bibliothèques django
from django.contrib import admin
from django.db import models
# Applications externes
from pagedown.widgets import AdminPagedownWidget
# Imports internes
from .models import Praticien, Office, ActCategory, Act, ActImage

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

class ActImageInline(admin.TabularInline):
    model = ActImage
    extra = 3
class ActAdmin(admin.ModelAdmin):
    inlines = [ ActImageInline, ]
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
admin.site.register(Act, ActAdmin)
