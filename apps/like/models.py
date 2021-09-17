from __future__ import unicode_literals
from django.db import models

class like(models.Model):

    id= models.TextField(),
    id_user = models.TextField()
    id_product = models.TextField()

    def __str__(self):
        return self.id