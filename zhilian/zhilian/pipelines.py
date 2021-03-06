# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from urllib import request
import pymongo

class ZhilianPipeline(object):
    def open_spider(self, spider):
        self.f = open("zhaopin.json", "a", encoding="utf-8")

    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item), indent=4, ensure_ascii=False) + ',\n')
        return item

    def close_spider(self, spider):
        self.f.close()


class MonPipeline(object):
    def open_spider(self,spider):
        self.conn= pymongo.MongoClient("localhost", 27017)
        self.db = self.conn.zhaopindb
        self.tables = self.db.zhaopintable
        self.tables.remove({})

    def process_item(self, item, spider):
        self.tables.insert(dict(item))
        return item

    def close_spider(self,spider):
        self.conn.close()