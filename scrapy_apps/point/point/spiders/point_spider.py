from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader.processors import MapCompose
from point.items import PointItem
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
from datetime import datetime

class PointCrawler(CrawlSpider):
    name = 'point'

    allowed_domains = ['point.com.ec']

    start_urls = ['https://point.com.ec/categoria-producto/tecnologia/laptops/']

    download_delay = 2

    # Tupla de reglas
    rules = (
        Rule(  # REGLA #1 => HORIZONTALIDAD POR PAGINACION
            LinkExtractor(
                allow=r'/page/d+'
            ), follow=True),
        Rule(
            LinkExtractor(
                allow=r'/producto/'
            ), follow=True, callback='parse_items'), )

    def parse_items(self, response):
        ap_item = PointItem()
        soup = BeautifulSoup(response.body)
        #identificador
        id = soup.find(class_="sku_wrapper")
        id_completo = id.text.replace('PORT', '').replace('\n', ' ').replace('\r', ' ').replace('SKU: ', '')
        ap_item['id'] = id_completo
        #titulo
        ap_item['titulo'] = response.xpath('//h1[@class="product_title entry-title"]/text()').extract_first()
        #descripción
        ap_item['descripcion'] = response.xpath('//div[@class="woocommerce-product-details'
                                                '__short-description"]/p/text()').extract()
        #fecha
        ap_item['fecha'] = datetime.today().strftime('%Y-%m-%d')
        #imagen
        ap_item['imagen'] = response.xpath('//figure[@class="woocommerce-product-gallery__wrapper"]'
                                           '/div/a/img/@src').extract_first()
        #link
        ap_item['link'] = response.xpath('/html/head/link[4]/@href').extract_first()

        #precio
        ap_item['precio'] = response.xpath('//*[@id="sticky-product-info-wapper"]/div'
                                           '/div/div[2]/p/span/text()').extract_first()

        yield ap_item