# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MercadoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    id = scrapy.Field()
    imagen = scrapy.Field()
    titulo = scrapy.Field()
    precio = scrapy.Field()
    descripcion = scrapy.Field()
