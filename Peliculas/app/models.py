from django.db import models

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    sinopsis = models.TextField()
    duracion = models.IntegerField()
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

