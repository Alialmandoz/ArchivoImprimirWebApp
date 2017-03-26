from django.db import models
from .choices import *


class Cliente(models.Model):
    nombre = models.CharField(max_length=200, blank=True)
    apellido = models.CharField(max_length=200, blank=True)
    mail = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=200, null=True, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.nombre + " " + self.apellido


class Ordenes(models.Model):
    tipo = models.IntegerField(choices=TIPO_TRABAJO)
    monto = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.get_tipo_display()) + " " + str(self.monto)