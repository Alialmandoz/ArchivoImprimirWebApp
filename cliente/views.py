from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.template.defaultfilters import slugify

from .models import Cliente, Ordenes
from .forms import ClienteForm, OrdenForm


def index(request):
    clientes = Cliente.objects.all()
    ordenes = Ordenes.objects.all()
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


def buscar_cliente(request):
        return render(request, 'cliente/buscar_cliente.html', {})


def resultado(request):
    a_buscar = request.GET.get('q')
    clientes = (get_list_or_404(Cliente, slug__icontains=a_buscar))
    ordenes = Ordenes.objects.all()
    return render(request, 'cliente/resultado.html', {'clientes': clientes, 'ordenes': ordenes})


def detalle_orden(request, pk):
    orden = get_object_or_404(Ordenes, pk=pk)
    return render(request, 'cliente/detalle_orden.html', {'orden': orden})


def crear_orden(request):
    if request.method == "POST":
        form = OrdenForm(request.POST)
        if form.is_valid():
            ordencreada = form.save()
            return redirect('orden', pk=ordencreada.pk)
    else:
        form = OrdenForm()
    return render(request, 'cliente/crear_orden.html', {'form': form})


def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            clientecreado = form.save(commit=False)
            clientecreado.slug = slugify(clientecreado.nombre + '-' + clientecreado.apellido)
            clientecreado = form.save()
            return redirect('detalleCliente', slug=slugify(clientecreado.nombre + '-' + clientecreado.apellido))
    else:
        form = ClienteForm()
    return render(request, 'cliente/crearcliente.html', {'form': form})