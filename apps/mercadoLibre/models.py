from __future__ import unicode_literals
from django.db import models

class mercadoLibre(models.Model):
<<<<<<< HEAD
=======
    id= models.TextField(),
>>>>>>> b93585f954aa12026bfef8f5d9e90b0345c64bd0
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