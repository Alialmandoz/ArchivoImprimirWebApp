from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    mail = models.EmailField()
    direccrion = models.CharField(max_length=200)
    telefono = models.IntegerField(max_length=20)
    ordenesTrabajos = models.ForeignKey(blank=True, null=True)

    def __str__(self):
        return self.nombre + " " + self.apellido