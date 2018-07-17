from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from .forms import PatientCreateForm
from .models import Patient


class ProPageView(TemplateView):
    template_name = "APP_002_PROPAGE/home-pro.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProPageView, self).get_context_data(*args, **kwargs)
        context['title'] = "Espace pro"
        return context

class PatientListView(ListView):
    template_name = "APP_002_PROPAGE/repertoire.html"

    def get_queryset(self):
        return Patient.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(PatientListView, self).get_context_data(*args, **kwargs)
        context['title'] = "Répertoire"
        return context

class PatientDetailView(DetailView):
    template_name = "APP_002_PROPAGE/patient_details.html"

    def get_queryset(self):
        return Patient.objects.all()

class PatientCreateView(CreateView):
    form_class = PatientCreateForm
    template_name = "APP_002_PROPAGE/patient_form.html"

class PatientDeleteView(DeleteView):
    model = Patient
    def get_success_url(self):
        return reverse("propage:espace-pro-repertoire")
