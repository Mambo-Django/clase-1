from django.db import models

class Usuario(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=32)  
    fecha_registro = models.DateField()
    edad = models.IntegerField()
    edad_padre = models.IntegerField(default=10)