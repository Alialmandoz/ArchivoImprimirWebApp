from django.db import models


class Mensaje(models.Model):
    nombre = models.CharField(max_length=200, blank=True)
    mail = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=200, null=True, blank=True)
    texto = models.TextField()

