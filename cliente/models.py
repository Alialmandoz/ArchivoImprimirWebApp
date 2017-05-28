from .choices import *
from django.contrib.admin.widgets import AdminDateWidget
from django.db import models
from django.db.models import DecimalField
from django.utils.datetime_safe import datetime


class Cliente(models.Model):
    nombre = models.CharField(max_length=200, blank=True)
    apellido = models.CharField(max_length=200, blank=True)
    mail = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=200, null=True, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return str(self.apellido)


class Ordenes(models.Model):
    fecha_encargo = models.DateField(default=datetime.now, blank=True)
    fecha_entrega = models.DateField(default=datetime.now, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cliente) + " " + str(self.fecha_entrega)


class Trabajo(models.Model):
    tipo = models.IntegerField(choices=TIPO_TRABAJO)
    detalle = models.TextField(null=True)
    monto = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    adelanto = DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    saldo = DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    orden = models.ForeignKey(Ordenes, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.get_tipo_display()) + " $" + str(self.monto)