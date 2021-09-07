from scrapy.spiders import CrawlSpider, Rule
from mercado.items import MercadoItem
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from datetime import datetime

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
        ml_item = MercadoItem()
        soup = BeautifulSoup(response.body)
        #identificador
        id = soup.find(class_="ui-pdp-color--BLACK ui-pdp-family--SEMIBOLD")
        id_completo = id.text.replace('#', '')
        ml_item['id'] = id_completo
        #codigo
        ml_item['codigo'] = id_completo
        #tienda
        ml_item['tienda'] = 'Mercado Libre'
        #titulo
        titulo = soup.find(class_="ui-pdp-title")
        titulo_completo = titulo.text.replace('\n', ' ').replace('\r', ' ')
        ml_item['titulo'] = titulo_completo
        #descripcion
        ml_item['descripcion'] = response.xpath('//*[@id="root-app"]/div/div[3]/div/div[2]/div[2]/div[3]/div/p/text()').extract()
        #fecha
        ml_item['fecha'] = datetime.today().strftime('%Y-%m-%d')
        #imagen
        ml_item['imagen'] = response.xpath('//*[@id="root-app"]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/span[1]/figure/img/@src').extract_first()
        ml_item['link'] = response.xpath('/html/head/link[14]/@href').extract_first()
        #precio
        precio = soup.find(class_="price-tag-fraction")
        precio_completo = precio.text.replace('\n', ' ').replace('\r', ' ').replace(' ', '')  # texto de todos los hijos
        ml_item['precio'] = precio_completo
        yield ml_item