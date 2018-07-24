# Bibliothèques django
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
# Imports internes
from .models import Praticien, Office, ActCategory, Act

# Vue qui affiche la page principale "home"
class ClientPageView(TemplateView):
    template_name = "APP_001_CLIENTPAGE/001_home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ClientPageView, self).get_context_data(*args, **kwargs)
        context['title'] = "Home"
        context['praticien'] = Praticien.objects.all().first()
        context['office'] = Office.objects.all().first()
        context['actscategories'] = ActCategory.objects.all()
        context['acte'] = Act.objects.all()
        return context

# Vue qui affiche les différentes vues détaillant les actes
class ActDetailView(DetailView):
    template_name = "APP_001_CLIENTPAGE/008_act_detail.html"

    def get_queryset(self):
        return Act.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ActDetailView, self).get_context_data(*args, **kwargs)
        context['praticien'] = Praticien.objects.all().first()
        context['actscategories'] = ActCategory.objects.all()
        return context
