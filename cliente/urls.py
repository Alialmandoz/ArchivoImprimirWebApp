from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detalle/(?P<slug>[-\w]+)/$', views.detalle_cliente, name='detalleCliente'),
    url(r'^detalle/(?P<slug>[-\w]+)/edit/$', views.editar_cliente, name='editarCliente'),
    url(r'^buscar_cliente/$', views.buscar_cliente, name='buscar_cliente'),
    url(r'^resultado_clientes/$', views.resultado, name='resultado'),
    url(r'^orden/(?P<pk>[-\d]+)/$', views.detalle_orden, name='orden'),
    url(r'^crear_orden/$', views.crear_orden, name='crear_orden'),
    url(r'^crear_cliente/$', views.crear_cliente, name='crear_cliente'),
    url(r'^simple/$', views.simple, name='simple'),


]