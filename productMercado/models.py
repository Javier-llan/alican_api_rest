from django.db import models

# Create your models here.
class Product(models.Model):
  titulo =models.CharField(max_length=150)
  descripcion = models.TextField(max_length=150)
  precio = models.CharField(max_length=150)

  class Meta:
    ordering = ['titulo']