from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader.processors import MapCompose
from almacenes_japon.items import JaponItem
from datetime import datetime
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

class LaGangaCrawler(CrawlSpider):
    name = 'almacenes_japon'

    allowed_domains = ['almacenesjapon.com']

    start_urls = ['https://almacenesjapon.com/20-computacion']

    download_delay = 2

    # Tupla de reglas
    rules = (
        Rule(
            LinkExtractor(
                allow=r'page=d+'
            ), follow=True),
        Rule(
            LinkExtractor(
                allow=r'/computacion/'
            ), follow=True, callback='parse_items'),)

    def parse_items(self, response):
        aj_item =  JaponItem()
        soup = BeautifulSoup(response.body)
        #identificador
        aj_item['id'] = response.xpath('//span[@class="item-code"]/text()').extract_first()
        #titulo
        aj_item['titulo'] = response.xpath('//h1[@class="h1 product-detail-name"]/text()').extract_first()
        #descripción
        aj_item['descripcion'] = response.xpath('//div[@id="product-description-short"]/p/text()').extract()
        #fecha
        aj_item['fecha'] = datetime.today().strftime('%Y-%m-%d')
        #imagen
        aj_item['imagen'] = response.xpath('//*[@id="thumbnails"]/div/div[1]/img/@src').extract_first()
        #link
        aj_item['link'] = response.xpath('/html/head/link[1]/@href').extract_first()
        #precio
        precio = response.xpath('//*[@id="main"]/div/div[2]/div[1]/div[1]/div/h4/text()').extract_first()
        precio_limpio = precio.replace('\n', ' ').replace('\r', ' ').replace('\t', '').replace('$', '')
        aj_item['precio'] = precio_limpio
        yield aj_item
        print(precio_limpio)