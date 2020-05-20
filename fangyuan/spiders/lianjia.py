# -*- coding: utf-8 -*-
import scrapy
from .. items import FangyuanItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['http://bj.lianjia.com/zufang//']

    def parse(self, response):
        data1 = response.xpath('//div[starts-with(@class,"content__article")]/p[@class="content__title"]/span/text()').extract_first()
        city_data = response.xpath('//div[starts-with(@class,"content__article")]/p[@class="content__title"]/a/text()').extract_first()
        item = FangyuanItem()
        item["data1"] = data1  # 租房数量
        item["city"] = city_data
        yield item

        base_url = "http://%s.lianjia.com/zufang//"
        for city in ["sh", "gz", "gz", "qd" ,"hz", "yt"]:
            full_url = base_url % city
            yield scrapy.Request(url=full_url, callback=self.parse)