from django.db import models

class MercadoItems(models.Model):
  titulo =models.CharField(max_length=150)
  descripcion = models.TextField(max_length=150)
  precio = models.CharField(max_length=150)

  class Meta:
    ordering = ['titulo']