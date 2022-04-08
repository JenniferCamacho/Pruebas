from typing_extensions import Self
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=100, null=False)
    descripcion=models.TextField(null=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        app_label='app'

class Pelicula(models.Model):
    titulo=models.CharField(max_length=500, null=False)
    year=models.IntegerField(null=True)
    # on_delete para que no se borre en cascada
    categoria=models.ForeignKey(Categoria, related_name='peliculas', null=False, on_delete=models.PROTECT)
    fecha_creacion=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label='app'
