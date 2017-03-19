from django.db import models
from .choices import *


class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre + " " + self.apellido


class Ordenes(models.Model):
    tipo = models.IntegerField(choices=TIPO_TRABAJO, default=1)
    monto = models.IntegerField(default=0)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tipo) + " " + str(self.monto)