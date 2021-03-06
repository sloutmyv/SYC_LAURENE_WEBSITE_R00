from django.conf.urls import url

from .views import (
    ProPageView,
    PatientListView,
    PatientDetailView,
    PatientCreateView,
    PatientDeleteView,
    PatientUpdateView,
)

urlpatterns = [
    url(r'^$', ProPageView.as_view(), name='espace-pro-home'),
    url(r'^repertoire/$', PatientListView.as_view(), name='espace-pro-repertoire'),
    url(r'^repertoire/create/$', PatientCreateView.as_view(), name='espace-pro-patient-form'),
    url(r'^repertoire/(?P<slug>[\w-]+)/$', PatientDetailView.as_view(), name='patient-details'),
    url(r'^repertoire/(?P<slug>[\w-]+)/delete/$', PatientDeleteView.as_view(), name='patient-delete'),
    url(r'^repertoire/(?P<slug>[\w-]+)/update/$', PatientUpdateView.as_view(), name='patient-update'),
]
