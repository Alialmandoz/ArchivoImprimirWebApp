from django.db import models




class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    mail = models.EmailField()
    direccrion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre + " " + self.apellido