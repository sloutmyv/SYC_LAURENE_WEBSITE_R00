from django.conf.urls import url

from .views import (
    LandingPageView,
)

urlpatterns = [
    url(r'^$', LandingPageView.as_view(), name='home'),
]
