from django.db import models
from ordenesTrabajo.models import Orden
# Create your models here.



class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    mail = models.EmailField()
    direccrion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    ordenes = models.ForeignKey(Orden)

    def __str__(self):
        return self.nombre + " " + self.apellido