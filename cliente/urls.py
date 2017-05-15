from django.conf.urls import url
from . import views

urlpatterns = [
    # inicio
    url(r'^$', views.index, name='index'),

    # resultado busqueda por letra
    url(r'^browse/(?P<letra>[-\w]+)/$', views.browse, name='browse'),

    # Crear cliente
    url(r'^crear_cliente/$', views.crear_cliente, name='crear_cliente'),

    # detalle del cliente
    url(r'^detalle/(?P<slug>[-\w]+)/$', views.detalle_cliente, name='detalleCliente'),

    # Borrar cliente
    url(r'^detalle/(?P<slug>[-\w]+)/edit/borrar/$', views.borrar_cliente, name='borrarCliente'),

    # alerta Borrar cliente
    url(r'^detalle/(?P<slug>[-\w]+)/edit/alerta/$', views.alerta_borrar_cliente, name='alertaBorrarCliente'),

    # editar cliente
    url(r'^detalle/(?P<slug>[-\w]+)/edit/$', views.editar_cliente, name='editarCliente'),

    # crear la orden
    url(r'^crear_orden/(?P<slug>[-\w]+)/$', views.crear_orden, name='crear_orden'),

    # detalle de la orden
    url(r'^orden/(?P<pk>[-\d]+)/$', views.detalle_orden, name='orden'),

    # editar la orden
    url(r'^orden/(?P<pk>[-\d]+)/edit/$', views.editar_orden, name='editarOrden'),

    # borrar la orden
    # url(r'^orden/(?P<pk>[-\d]+)/borrar/$', views.borrar_orden, name='borrarOrden'),

    # calculadora de precios
    url(r'^calculador/$', views.calculador, name='calculador'),

]