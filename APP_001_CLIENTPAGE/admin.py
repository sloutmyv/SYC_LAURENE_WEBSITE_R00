from django.contrib import admin
from django.db import models

from pagedown.widgets import AdminPagedownWidget

from .models import Praticien, Office, ActCategory, Act, ActImage

## Admin for Praticien model
class PraticienAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(Praticien, PraticienAdmin)

## Admin for Office model
class OfficeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(Office, OfficeAdmin)

## Admin for ActCategory model
class ActCategoryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(ActCategory, ActCategoryAdmin)

## Admin for Act model
class ActImageInline(admin.TabularInline):
    model = ActImage
    extra = 3

class ActAdmin(admin.ModelAdmin):
    inlines = [ ActImageInline, ]
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(Act, ActAdmin)
