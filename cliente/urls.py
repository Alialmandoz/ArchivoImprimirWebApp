from django.conf.urls import url
from . import views

urlpatterns = [
    # inicio
    url(r'^inicio$', views.buscar_por_ordenes, name='index'),

    # resultado busqueda por letra
    url(r'^browse/(?P<letra>[-\w]+)/$', views.browse, name='browse'),

    # ########################## Cliente ########################## #

    # Crear cliente
    url(r'^crear_cliente/$', views.crear_cliente, name='crear_cliente'),

    # detalle del cliente
    url(r'^detalle/(?P<slug>[-\w]+)/$', views.detalle_cliente, name='detalleCliente'),

    # buscar la orden
    url(r'^cliente/buscar/$', views.buscar_por_cliente, name='buscar_por_cliente'),

    # Borrar cliente
    url(r'^detalle/(?P<slug>[-\w]+)/edit/borrar/$', views.borrar_cliente, name='borrarCliente'),

    # alerta Borrar cliente
    url(r'^detalle/(?P<slug>[-\w]+)/edit/alerta/$', views.alerta_borrar_cliente, name='alertaBorrarCliente'),

    # editar cliente
    url(r'^detalle/(?P<slug>[-\w]+)/edit/$', views.editar_cliente, name='editarCliente'),

    # ########################## Orden ########################## #

    # crear la orden
    url(r'^crear_orden/(?P<slug>[-\w]+)/$', views.crear_orden, name='crear_orden'),

    # detalle de la orden
    url(r'^orden/(?P<pk>[-\d]+)/$', views.detalle_orden, name='orden'),

    # editar la orden
    url(r'^orden/(?P<pk>[-\d]+)/edit/$', views.editar_orden, name='editarOrden'),

    # buscar la orden
    url(r'^orden/buscar/$', views.buscar_por_ordenes, name='buscar_por_ordenes'),

    # alerta Borrar orden
    url(r'^orden/(?P<pk>[-\d]+)/edit/alerta/$', views.alerta_borrar_orden, name='alertaBorrarOrden'),

    # borrar la orden
    url(r'^orden/(?P<pk>[-\d]+)/borrar/$', views.borrar_orden, name='borrarOrden'),

    # ########################## Trabajo ########################## #

    # crear trabajo
    url(r'^crear_trabajo/(?P<pk>[-\d]+)/$', views.crear_trabajo, name='crear_trabajo'),

    # detalle trabajo
    url(r'^trabajo/(?P<pk>[-\d]+)/$', views.detalle_trabajo, name='trabajo'),

    # editar trabajo
    url(r'^trabajo/(?P<pk>[-\d]+)/edit/$', views.editar_trabajo, name='editar_trabajo'),

    # alerta Borrar trabajo
    url(r'^trabajo/(?P<pk>[-\d]+)/edit/alerta/$', views.alerta_borrar_trabajo, name='alerta_borrar_trabajo'),

    # borrar trabajo
    url(r'^trabajo/(?P<pk>[-\d]+)/borrar/$', views.borrar_trabajo, name='borrar_trabajo'),


    # calculadora de precios
    url(r'^calculador/$', views.calculador, name='calculador'),

    # contacto
    url(r'^contacto/$', views.contacto, name='contacto'),

]