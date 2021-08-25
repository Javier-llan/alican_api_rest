from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader.processors import MapCompose
from mercado.items import MercadoItem
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

class MercadoLibreCrawler(CrawlSpider):
    name = 'mercadoLibre'

    allowed_domains = ['articulo.mercadolibre.com.ec', 'listado.mercadolibre.com.ec']

    start_urls = ['https://listado.mercadolibre.com.ec/computacion-notebooks/']

    download_delay = 2

    # Tupla de reglas
    rules = (
        Rule(  # REGLA #1 => HORIZONTALIDAD POR PAGINACION
            LinkExtractor(
                allow=r'/_Desde_\d+'
            ), follow=True),
        Rule(
            LinkExtractor(
                allow=r'/MEC-43'
            ), follow=True, callback='parse_items'), )

    def parse_items(self, response):
        item = ItemLoader(MercadoItem(), response)

        # Utilizo Map Compose con funciones anonimas
        item.add_xpath('id', '//span[@class="ui-pdp-color--BLACK ui-pdp-family--SEMIBOLD"]/text()')
        item.add_xpath('titulo', '//h1/text()', MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))
        item.add_xpath('descripcion', '//div[@class="ui-pdp-description"]/p/text()',
                       MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))
        item.add_xpath('imagen', '//*[@id="root-app"]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/span[1]/figure/img/@src')
        soup = BeautifulSoup(response.body)

        precio = soup.find(class_="price-tag-fraction")
        precio_completo = precio.text.replace('\n', ' ').replace('\r', ' ').replace(' ', '')  # texto de todos los hijos
        item.add_value('precio', precio_completo)

        yield item.load_item()