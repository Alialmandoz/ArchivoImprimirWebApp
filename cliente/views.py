from django.shortcuts import render, get_object_or_404
from .models import Cliente
from .models import Ordenes

def index(request):
    clientes = Cliente.objects.all()
    ordenes = Ordenes.objects.all()
    return render(request, 'cliente/index.html', {'clientes': clientes, 'ordenes': ordenes})


def detalle_cliente(request, slug):
    cliente = get_object_or_404(Cliente, slug=slug)
    ordenes = Ordenes.objects.all()
    return render(request, 'cliente/detalleCliente.html', {'cliente': cliente, 'ordenes': ordenes})