from mongoengine import *

class MercadoItems(Document):
    titulo = StringField()
    descripcion = StringField()
    precio = StringField()

    def __str__(self):
        return self.titulo