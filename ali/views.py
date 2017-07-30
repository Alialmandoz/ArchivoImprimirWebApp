from django.shortcuts import render
from ali.models import Mensaje

from .forms import MensajeForm


def home(request):
    return render(request, 'ali/home.html')


def work(request):
    return render(request, 'ali/work.html')


def contact(request):
    if request.method == "POST":
        form = MensajeForm(request.POST or None)
        if form.is_valid():
            form.save()
            print('guardando msj')
            mensajes = Mensaje.objects.all()
        return render(request, 'ali/contacto.html', {'form': form, 'mensajes': mensajes})
    else:
        mensajes = Mensaje.objects.all()
        form = MensajeForm()
    return render(request, 'ali/contacto.html', {'form': form, 'mensajes': mensajes})


def about(request):
    return render(request, 'ali/about_me.html')


def gracias(request):
    return render(request, 'ali/gracias.html')