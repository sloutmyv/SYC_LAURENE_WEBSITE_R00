from django.conf.urls import url

from .views import (
    ProPageView,
    PatientListView,
)

urlpatterns = [
    url(r'^$', ProPageView.as_view(), name='espace-pro-home'),
    url(r'^repertoire/$', PatientListView.as_view(), name='espace-pro-repertoire'),
]
