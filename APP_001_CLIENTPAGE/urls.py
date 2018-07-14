from django.conf.urls import url

from .views import (
    ClientPageView,
    ActDetailView,
)

urlpatterns = [
    url(r'^$', ClientPageView.as_view(), name='home'),
    url(r'^(?P<slug>[\w-]+)/$', ActDetailView.as_view(), name='act-details'),
]
