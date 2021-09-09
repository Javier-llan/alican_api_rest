# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import pymongo
from scrapy.exceptions import DropItem


class mongoDB_pipeline:
    
    def __init__(self, mongo_uri, mongo_db, collection_name):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection_name = collection_name
        self.ids_seen = set()

    @classmethod
    def from_crawler(cls, crawler):
        #mongo_uri, mongo_db, collection_name are from settings.py
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            collection_name=crawler.settings.get('COLLECTION_NAME')
        )

    #initialize spider and open db connection
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    
    #close spider
    def close_spider(self, spider):
        self.client.close()

    #get scrapped data into collection
    def process_item(self, item, spider):
        mcDict = {}
        if item['id'] in self.ids_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            mcDict['id'] = item['id']
            mcDict['codigo'] = item['codigo']
            mcDict['tienda'] = item['tienda']
            mcDict['titulo'] = item['titulo']
            mcDict['descripcion'] = item['descripcion']
            mcDict['precio'] = item['precio']
            mcDict['imagen'] = item['imagen']
            mcDict['link'] = item['link']
            mcDict['fecha'] = item['fecha']
            self.db[self.collection_name].insert_one(dict(mcDict))
            logging.debug('title added to mongoDB')
            return item


