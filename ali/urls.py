from django.conf.urls import url
from . import views

urlpatterns = [
    # inicio
    url(r'^$', views.home, name='index'),
    url(r'^work/$', views.work, name='work'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^gracias/$', views.gracias, name='gracias'),

]