from django.db import models

class Publicacion(models.Model):
    titulo = models.CharField( max_length=20)
    descripcion = models.CharField(max_length = 50)
    fecha = models.DateField()
    lugar = models.CharField(max_length = 30)
    imagen = models.ImageField( upload_to="static/imagenes", null = True)


