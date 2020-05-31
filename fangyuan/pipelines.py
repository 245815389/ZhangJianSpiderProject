# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
from urllib import request
import pymongo

class FangyuanPipeline(object):
    def open_spider(self, spider):
        self.f = open("fangyuan.json", "a", encoding="utf-8")

    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item), indent=4, ensure_ascii=False) + ',\n')
        return item

    def close_spider(self, spider):
        self.f.close()

class MonPipeline(object):
    def open_spider(self,spider):
        self.conn= pymongo.MongoClient("localhost", 27017)
        self.db = self.conn.fangyuandb
        self.tables = self.db.fangyuantable
        self.tables.remove({})

    def process_item(self, item, spider):
        self.tables.insert(dict(item))
        return item

    def close_spider(self,spider):
        self.conn.close()

 #    --------------------------------------------------------info--------------------------------------------------------------------
class FangyuaninfoPipeline(object):
    def open_spider(self, spider):
        self.f = open("fangyuaninfo.json", "a", encoding="utf-8")

    def process_item(self, info_item, spider):
        self.f.write(json.dumps(dict(info_item), indent=4, ensure_ascii=False) + ',\n')
        return info_item

    def close_spider(self, spider):
        self.f.close()

class MoninfoPipeline(object):
    def open_spider(self,spider):
        self.conn= pymongo.MongoClient("localhost", 27017)
        self.db = self.conn.fangyuaninfodb
        self.tables = self.db.fangyuaninfotable
        self.tables.remove({})

    def process_item(self, info_item, spider):
        self.tables.insert(dict(info_item))
        return info_item

    def close_spider(self,spider):
        self.conn.close()