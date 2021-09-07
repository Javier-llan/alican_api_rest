from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader.processors import MapCompose
from comandato.items import ComandatoItem
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from datetime import datetime
from scrapy.loader import ItemLoader

class LaGangaCrawler(CrawlSpider):
    name = 'comandato'

    allowed_domains = ['comandato.com']

    start_urls = ['https://www.comandato.com/electrodomesticos/refrigeracion/refrigeradoras']

    download_delay = 2

    # Tupla de reglas
    rules = (
        Rule(
            LinkExtractor(
                allow=r'/refrigeradora-'
            ), follow=True, callback='parse_items'),)

    def parse_items(self, response):
        #Datos scraping
        cm_item = ComandatoItem()
        soup = BeautifulSoup(response.body)
        #identificador
        cm_item['id'] = response.xpath('//div[@class="skuReference"]/text()').extract_first()
        #titulo
        cm_item['titulo'] = response.xpath('/html/head/title/text()').extract_first()
        #descripcion
        descripcion = soup.find(class_="content-ficha")
        descripcion_completa = descripcion.text.replace('\n', '')
        cm_item['descripcion'] = descripcion_completa
        #fecha
        cm_item['fecha'] = datetime.today().strftime('%Y-%m-%d')
        #imagen
        cm_item['imagen'] = response.xpath('//*[@id="image-main"]/@src').extract_first()
        #link
        cm_item['link'] = response.xpath('/html/head/link[6]/@href').extract_first()
        #precio

        cm_item['precio'] = response.xpath('//*[@id="2021-producto-new"]/main/section[2]/div[2]'
                                           '/div[2]/span/text()').extract_first()
        yield cm_item
