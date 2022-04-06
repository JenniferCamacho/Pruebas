from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=100, null=False)
    descripcion=models.TextField(null=True)

    class Meta:
        app_label='app'
        