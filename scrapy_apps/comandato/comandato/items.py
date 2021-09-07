# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ComandatoItem(scrapy.Item):
    # define the fields for your item here like:
    #pass
    id = scrapy.Field()
    imagen = scrapy.Field()
    titulo = scrapy.Field()
    fecha = scrapy.Field()
    precio = scrapy.Field()
    descripcion = scrapy.Field()
    link = scrapy.Field()
