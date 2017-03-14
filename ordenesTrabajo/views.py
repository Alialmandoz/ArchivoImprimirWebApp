from django.shortcuts import render, get_object_or_404
from .models import Orden


def orden(request, pk):
    orden = get_object_or_404(Orden, pk=pk)
    return render(request, 'orden/orden.html', {'orden': orden})