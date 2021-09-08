from __future__ import unicode_literals
from django.db import models

class mercadoLibre(models.Model):

    id= models.TextField(),
    titulo = models.TextField()
    codigo = models.TextField(max_length=250, default='SOME STRING')
    tienda = models.TextField(max_length=250,default='SOME STRING')
    descripcion = models.TextField()
    imagen = models.TextField()
    precio = models.TextField()
    link = models.CharField(max_length=250,default='SOME STRING')
    fecha = models.CharField(max_length=250,default='SOME STRING')

    def __str__(self):
        return self.titulo