import cliente
from django.shortcuts import get_object_or_404, redirect, get_list_or_404
from django.template.defaultfilters import slugify
from .models import Cliente, Ordenes
from .forms import ClienteForm, OrdenForm, Calculador
from cliente import choices
from django.shortcuts import render


def paginas(model):
    todas_letras = 'abcdefghijklmnopqrstuvwxyz'
    letras = []
    for i in model:
        for l in todas_letras:
            list_does_contain = next((True for item in letras if item == l.lower()), False)
            if i.apellido.lower().startswith(l.lower()) and not list_does_contain:
                letras.append(str(l).lower())
    return letras


def index(request):
    letra = 'a'
    a_buscar = request.GET.get('q')
    clientes = Cliente.objects.order_by('apellido')
    letras = paginas(clientes)
    ordenes = Ordenes.objects.all()
    if a_buscar is not None:
        clientes = (get_list_or_404(Cliente, slug__icontains=a_buscar))
        return render(request, 'cliente/index.html',
                      {'clientes': clientes, 'ordenes': ordenes, 'letras': letras, 'letra': letra})
    return render(request, 'cliente/index.html',
                  {'clientes': clientes, 'ordenes': ordenes, 'letras': letras, 'letra': letra})


def browse(request, letra):
    clientes = Cliente.objects.order_by('apellido')
    letras = paginas(clientes)
    ordenes = Ordenes.objects.all()
    if letra:
        clientes = (get_list_or_404(Cliente, apellido__startswith=letra))
        ordenes = Ordenes.objects.all()
        return render(request, 'cliente/index.html',
                      {'clientes': clientes, 'ordenes': ordenes, 'letras': letras, 'letra': letra})
    return render(request, 'cliente/index.html',
                  {'clientes': clientes, 'ordenes': ordenes, 'letras': letras, 'letra': letra})


def detalle_cliente(request, slug):
    cliente = get_object_or_404(Cliente, slug=slug)
    ordenes = Ordenes.objects.all()
    return render(request, 'cliente/detalleCliente.html', {'cliente': cliente, 'ordenes': ordenes})


def editar_cliente(request, slug):
    cliente = Cliente.objects.get(slug=slug)
    form_class = ClienteForm
    if request.method == 'POST':
        form = form_class(data=request.POST or None, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('detalleCliente', slug=cliente.slug)
    else:
        form = form_class(instance=cliente)

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


def crear_orden(request, slug):
    form = OrdenForm(request.POST or None)
    if request.method == "POST":
        cli = Cliente.objects.get(slug=slug)
        if form.is_valid():
            ordencreada = form.save(commit=False)
            ordencreada.cliente = cli
            ordencreada = form.save()
            return redirect('orden', pk=ordencreada.pk)
        else:
            form = OrdenForm()
    return render(request, 'cliente/crear_orden.html', {'form': form})


def crear_orden2(request):
    if request.method == "POST":
        form = OrdenForm(request.POST or None)
        if form.is_valid():
            ordencreada = form.save()
            return redirect('orden', pk=ordencreada.pk)
    else:
        form = OrdenForm()
    return render(request, 'cliente/crear_orden.html', {'form': form})


def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST or None)
        if form.is_valid():
            clientecreado = form.save(commit=False)
            clientecreado.slug = slugify(clientecreado.nombre + '-' + clientecreado.apellido)
            clientecreado = form.save()
            return redirect('detalleCliente', slug=slugify(clientecreado.nombre + '-' + clientecreado.apellido))
    else:
        form = ClienteForm()
    return render(request, 'cliente/crearcliente.html', {'form': form})


def calculador(request):
    if request.method == 'GET':
        print('el metodo es get')
        form = Calculador(request.GET or None)
        if form.is_valid():
            print('la forma es valida')
            cantidad = form.cleaned_data['cantidad']
            material = form.cleaned_data['soporte']
            print('material ' + material)
            caras = form.cleaned_data['impresion']
            calcular = form.calcular(material, cantidad, caras)
            material = choices.traducir_soporte(material)
            print('material traducido  ' + material)
            caras = choices.traducir_cara(caras)
            return render(request, 'cliente/calculador.html',
                          {'form': form, 'calcular': calcular, "material": material, "caras": caras})
        else:
            print('la forma no es valida')
            return render(request, 'cliente/calculador.html', {'form': form})
    print('el principio de la historia')
    return render(request, 'cliente/calculador.html')


