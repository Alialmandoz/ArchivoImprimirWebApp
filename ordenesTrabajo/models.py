from django.db import models

# Create your models here.


class Orden(models.Model):
    cliente = models.CharField(max_length=200)
    trabajos = models.CharField(max_length=200)
    total = models.IntegerField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.pk + " " + self.cliente