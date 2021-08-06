from django.db import models

class Products(models.Model):

    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    precio = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo