from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import PatientCreateForm
from .models import Patient


class ProPageView(TemplateView):
    template_name = "APP_002_PROPAGE/001_home_pro.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProPageView, self).get_context_data(*args, **kwargs)
        context['title'] = "Espace pro"
        return context

class PatientListView(ListView):
    template_name = "APP_002_PROPAGE/003_repertoire.html"

    def get_queryset(self):
        return Patient.objects.all().order_by('patient_last_name')

    def get_context_data(self, *args, **kwargs):
        context = super(PatientListView, self).get_context_data(*args, **kwargs)
        context['title'] = "Répertoire"
        return context

class PatientDetailView(DetailView):
    template_name = "APP_002_PROPAGE/004_patient_details.html"

    def get_queryset(self):
        return Patient.objects.all()

class PatientCreateView(CreateView):
    form_class = PatientCreateForm
    template_name = "APP_002_PROPAGE/005_patient_form.html"

    def get_context_data(self,*args,**kwargs):
        context = super(PatientCreateView, self).get_context_data(*args,**kwargs)
        context['title'] = 'Nouvelle patiente'
        return context

class PatientDeleteView(DeleteView):
    model = Patient
    def get_success_url(self):
        return reverse("propage:espace-pro-repertoire")

class PatientUpdateView(UpdateView):
    form_class = PatientCreateForm
    template_name = 'APP_002_PROPAGE/006_patient_update.html'

    def get_context_data(self,*args,**kwargs):
        context = super(PatientUpdateView, self).get_context_data(*args,**kwargs)
        context['title'] = 'Mise à jour'
        return context

    def get_queryset(self):
        return Patient.objects.all()
