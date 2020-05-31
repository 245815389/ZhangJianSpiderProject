# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class FangyuanItem(scrapy.Item):
    # define the fields for your item here like:
    city = scrapy.Field()
    data1 = scrapy.Field()



class info_FangyuanItem(scrapy.Item):
    information1 = scrapy.Field()
    information2 = scrapy.Field()
    information3 = scrapy.Field()
    title = scrapy.Field()
