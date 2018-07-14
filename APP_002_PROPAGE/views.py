from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.views.generic import ListView

from .models import Patient


class ProPageView(TemplateView):

    template_name = "APP_002_PROPAGE/pro_home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProPageView, self).get_context_data(*args, **kwargs)
        context['title'] = "Espace pro"
        return context

class PatientListView(ListView):

    template_name = "APP_002_PROPAGE/pro_repertoire.html"

    def get_queryset(self):
        return Patient.objects.all()
