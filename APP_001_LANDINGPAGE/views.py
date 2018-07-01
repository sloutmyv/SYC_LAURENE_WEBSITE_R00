from django.shortcuts import render
from django.views.generic.base import TemplateView


class LandingPageView(TemplateView):

    template_name = "APP_001_LANDINGPAGE/home.html"
