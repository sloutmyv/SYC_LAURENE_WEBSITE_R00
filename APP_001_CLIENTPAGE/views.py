from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Praticien

class ClientPageView(TemplateView):

    template_name = "APP_001_CLIENTPAGE/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ClientPageView, self).get_context_data(*args, **kwargs)
        context['title'] = "Home"
        context['praticien'] = Praticien.objects.all().first()
        return context
