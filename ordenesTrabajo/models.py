from django.db import models
from cliente.models import Cliente


class Orden(models.Model):
    trabajos = models.CharField(max_length=200)
    total = models.IntegerField()
    cliente = models.ForeignKey(Cliente, blank=True, null=True)

    def __str__(self):
        title = (str(self.pk))
        return title