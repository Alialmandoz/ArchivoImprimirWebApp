from django.shortcuts import get_object_or_404, redirect, get_list_or_404
from django.template.defaultfilters import slugify
from .models import Cliente, Ordenes, Trabajo
from .forms import ClienteForm, OrdenForm, Calculador, TrabajoForm
from cliente import choices
from django.shortcuts import render

# ################################# login ######################################################## #

# ################################# Inicio ######################################################## #


def paginas(model):
    model

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
    a_buscar = request.GET.get('busqueda')
    clientes = Cliente.objects.order_by('apellido')
    letras = paginas(clientes)
    ordenes = Ordenes.objects.all()
    if request.user.is_authenticated:
        if a_buscar is not None:
            clientes = (get_list_or_404(Cliente, slug__icontains=a_buscar))
            return render(request, 'cliente/index.html',
                      {'clientes': clientes, 'ordenes': ordenes, 'letras': letras, 'letra': letra})
        return render(request, 'cliente/index.html',
                  {'clientes': clientes, 'ordenes': ordenes, 'letras': letras, 'letra': letra})
    return redirect('login')


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


# ################################# cliente ######################################################## #


def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST or None)
        if form.is_valid():
            clientecreado = form.save(commit=False)
            clientecreado.apellido = str(clientecreado.apellido).capitalize()
            clientecreado.slug = slugify(clientecreado.nombre + '-' + clientecreado.apellido)
            clientecreado = form.save()
            print('el apellido es: ' + clientecreado.apellido)
            return redirect('detalleCliente', slug=slugify(clientecreado.nombre + '-' + clientecreado.apellido))
    else:
        form = ClienteForm()
    return render(request, 'cliente/crear_cliente.html', {'form': form})


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

    return render(request, 'Cliente/editar_cliente.html', {'cliente': cliente, 'form': form})


def detalle_cliente(request, slug):
    cliente = get_object_or_404(Cliente, slug=slug)
    ordenes = Ordenes.objects.all()
    return render(request, 'cliente/detalle_cliente.html', {'cliente': cliente, 'ordenes': ordenes})


def alerta_borrar_cliente(request, slug):
    cliente = get_object_or_404(Cliente, slug=slug)
    return render(request, 'cliente/alerta_borrar_cliente.html', {'cliente': cliente})


def borrar_cliente(request, slug):
    cliente = get_object_or_404(Cliente, slug=slug).delete()
    return redirect(index)


# ########################################### orden ###################################################### #


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
    return render(request, 'orden/crear_orden.html', {'form': form})


def editar_orden(request, pk):
    orden = get_object_or_404(Ordenes, pk=pk)
    form_class = OrdenForm

    if request.method == 'POST':
        form = form_class(data=request.POST or None, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('orden', orden.pk)
    else:
        form = form_class(instance=orden)

    return render(request, 'orden/editar_orden.html', {'orden': orden, 'form': form})


def detalle_orden(request, pk):
    orden = get_object_or_404(Ordenes, pk=pk)
    trabajos = orden.trabajo_set.all()
    form = TrabajoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            trabajo_creado = form.save(commit=False)
            trabajo_creado.orden = orden
            trabajo_creado = form.save()
            return redirect('orden', pk=orden.pk)
        else:
            form = TrabajoForm()
    return render(request, 'orden/detalle_orden.html', {'orden': orden, 'trabajos': trabajos, 'form': form})


def alerta_borrar_orden(request, pk):
    orden = get_object_or_404(Ordenes, pk=pk)
    return render(request, 'orden/alerta_borrar_orden.html', {'orden': orden})


def borrar_orden(request, pk):
    orden = get_object_or_404(Ordenes, pk=pk).delete()
    return redirect(index)


# ########################################### trabajo ###################################################### #


def crear_trabajo(request, pk):
    form = TrabajoForm(request.POST or None)
    if request.method == "POST":
        orden = Ordenes.objects.get(pk=pk)
        if form.is_valid():
            trabajocreado = form.save(commit=False)
            trabajocreado.orden = orden
            trabajocreado = form.save()
            return redirect('orden', pk=orden.pk)
        else:
            form = TrabajoForm()
    return render(request, 'trabajo/crear_trabajo.html', {'form': form})


def editar_trabajo(request, pk):
    trabajo = get_object_or_404(Trabajo, pk=pk)
    form_class = TrabajoForm

    if request.method == 'POST':
        form = form_class(data=request.POST or None, instance=trabajo)
        if form.is_valid():
            form.save()
            return redirect('trabajo', trabajo.pk)
    else:
        form = form_class(instance=trabajo)

    return render(request, 'trabajo/editar_trabajo.html', {'trabajo': trabajo, 'form': form})


def detalle_trabajo(request, pk):
    trabajo = get_object_or_404(Trabajo, pk=pk)
    return render(request, 'trabajo/detalle_trabajo.html', {'trabajo': trabajo})


def alerta_borrar_trabajo(request, pk):
    trabajo = get_object_or_404(Trabajo, pk=pk)
    return render(request, 'trabajo/alerta_borrar_trabajo.html', {'trabajo': trabajo})


def borrar_trabajo(request, pk):
    trabajo = get_object_or_404(Trabajo, pk=pk).delete()
    return redirect(index)


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


