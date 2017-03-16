from django.db import models


class Orden(models.Model):
    trabajos = models.CharField(max_length=200)
    total = models.IntegerField()

    def __str__(self):
        title = ("orden de Trabajo: " + str(self.pk) + " = " + str(self.trabajos) + " :$" + str(self.total))
        return title