from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^things/(?P<slug>[-\w]+)/$', views.detalle_cliente, name='detalleCliente'),
]


''' url(r'^detalle/(?P<pk>\d+)/$', views.detalle_cliente, name='detalleCliente'),'''