from django.shortcuts import render, get_object_or_404
from .models import Cliente


def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/index.html', {'clientes': clientes})


def detalle_cliente(request, nombre):
    cliente = get_object_or_404(Cliente, nombre=nombre)

    return render(request, 'cliente/detalleCliente.html', {'cliente': cliente})