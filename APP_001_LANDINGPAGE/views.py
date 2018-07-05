from django.shortcuts import render
from django.views.generic.base import TemplateView


from .models import InfosProfessionnelles, CategoriesActes

class LandingPageView(TemplateView):

    template_name = "APP_001_LANDINGPAGE/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(LandingPageView, self).get_context_data(*args, **kwargs)
        context['title'] = "Home"
        context['infosprofessionnelles'] = InfosProfessionnelles.objects.all().first()
        context['categorieactes'] = CategoriesActes.objects.all()
        return context
