# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JaponItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    codigo = scrapy.Field()
    tienda = scrapy.Field()
    imagen = scrapy.Field()
    titulo = scrapy.Field()
    precio = scrapy.Field()
    descripcion = scrapy.Field()
    fecha = scrapy.Field()
    link = scrapy.Field()
