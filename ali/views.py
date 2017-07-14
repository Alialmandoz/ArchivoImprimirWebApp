from django.shortcuts import render

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
        return render(request, 'ali/gracias.html')
    else:
        form = MensajeForm()
    return render(request, 'ali/contact.html', {'form': form})


def about(request):
    return render(request, 'ali/about_me.html')


def gracias(request):
    return render(request, 'ali/gracias.html')