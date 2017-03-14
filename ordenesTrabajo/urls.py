from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^orden/(?P<pk>\d+)/$', views.orden, name='detalleOrden'),
]


''' url(r'^detalle/(?P<pk>\d+)/$', views.detalle_cliente, name='detalleCliente'),'''