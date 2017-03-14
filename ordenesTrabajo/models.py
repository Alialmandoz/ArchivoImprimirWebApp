from django.db import models
from cliente.models import Cliente


class Orden(models.Model):
    cli = models.ForeignKey(Cliente)
    trabajos = models.CharField(max_length=200)
    total = models.IntegerField()

    def __str__(self):
        return self.pk + " " + self.cliente