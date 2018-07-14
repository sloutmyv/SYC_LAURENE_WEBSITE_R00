from django.conf.urls import url

from .views import (
    ClientPageView,
    ActDetailView,
)

urlpatterns = [
    url(r'^$', ClientPageView.as_view(), name='client-page-home'),
    url(r'^(?P<slug>[\w-]+)/$', ActDetailView.as_view(), name='acte-details'),
]
