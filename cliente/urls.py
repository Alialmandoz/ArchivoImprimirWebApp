from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detalle/(?P<slug>[-\w]+)/$', views.detalle_cliente, name='detalleCliente'),
]


''' '''