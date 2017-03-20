from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Cliente
from .models import Ordenes
from .forms import ClienteForm


ordenes = Ordenes.objects.all()


def index(request):
    clientes = Cliente.objects.all()

    return render(request, 'cliente/index.html', {'clientes': clientes, 'ordenes': ordenes})


def detalle_cliente(request, slug):
    cliente = get_object_or_404(Cliente, slug=slug)
    ordenes = Ordenes.objects.all()
    return render(request, 'cliente/detalleCliente.html', {'cliente': cliente, 'ordenes': ordenes})


def editar_cliente(request, slug):
    # grab the object
    cliente = Cliente.objects.get(slug=slug)
    # set the form we're using
    form_class = ClienteForm

    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to
        # the form
        form = form_class(data=request.POST, instance=cliente)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('detalleCliente', slug=cliente.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=cliente)

    # and render the template
    return render(request, 'Cliente/editarCliente.html', {'cliente': cliente, 'form': form})


def buscar(request):
    a_buscar = request.GET.get('q')
    print('a_buscar: ' + a_buscar)
    clientes = (get_list_or_404(Cliente, slug__icontains=a_buscar))
    print('largo: ' + str(len(clientes)))
    print(clientes)

    return render(request, 'cliente/resultado.html', {'clientes': clientes, 'ordenes': ordenes})