from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detalle/(?P<slug>[-\w]+)/$', views.detalle_cliente, name='detalleCliente'),
    url(r'^detalle/(?P<slug>[-\w]+)/edit/$', views.editar_cliente, name='editarCliente'),
    url(r'^buscar/$', views.buscar, name='buscar'),
    url(r'^orden/(?P<pk>[-\d]+)/$', views.detalle_orden, name='orden'),
    url(r'^crear_orden/$', views.crear_orden, name='crear_orden'),


]