from django.conf.urls import url

from .views import (
    ClientPageView,
)

urlpatterns = [
    url(r'^$', ClientPageView.as_view(), name='home'),
]
