from django.conf.urls import url
from . import views

urlpatterns = [
    # inicio
    url(r'^$', views.home, name='home'),
    url(r'^work/$', views.work, name='work'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
]