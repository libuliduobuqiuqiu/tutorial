# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):
    def __init__(self, datafile_path):
        self.datafile_path = datafile_path

    @classmethod
    def from_crawler(cls, crawler):
        return cls(datafile_path = crawler.settings.get("DATAFILE_PATH"))
    
    def open_spider(self, spider):
        spider_name = spider.name+".json"
        file_path = self.datafile_path + "/" + spider_name
        self.file = open(file_path, 'w+')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(line + " \n")
        return item

    def spider_closed(self, spider):
        self.file.close()


class MongoPipeline(object):
    collections_name = "tencent_jobs"
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri = crawler.settings.get('MONGO_URI'), 
                mongo_db = crawler.settings.get("MONGO_DATABASE"))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collections_name].insert(dict(item))
        return item
        
        


