from django.shortcuts import render
from django.views.generic.base import TemplateView


class LandingPageView(TemplateView):

    template_name = "APP_001_LANDINGPAGE/home.html"

    def get_context_data(self, **kwargs):
        context = super(LandingPageView, self).get_context_data(**kwargs)
        context['title'] = "Home"
        return context
