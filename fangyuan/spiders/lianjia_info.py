# -*- coding: utf-8 -*-
import scrapy
from .. items import info_FangyuanItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia_info'
    allowed_domains = ['lianjia.com']
    start_urls = ['http://bj.lianjia.com/zufang//']
    custom_settings = {
        'ITEM_PIPELINES' : {
            'fangyuan.pipelines.FangyuaninfoPipeline': 400,
            'fangyuan.pipelines.MoninfoPipeline': 400,
        }
    }

    def parse(self, response):
        div_list = response.xpath('//div[@class="content__list--item"]')
        for div in div_list:
            info_item = info_FangyuanItem()
            title = div.xpath('./div[starts-with(@class,"content__list--item--main")]/p[1]/a/text()').extract_first()
            informaton1 = div.xpath('./div[starts-with(@class,"content__list--item--main")]/p[2]/a[1]/text()').extract_first()
            informaton2 = div.xpath('./div[starts-with(@class,"content__list--item--main")]/p[2]/a[2]/text()').extract_first()
            informaton3 = div.xpath('./div[starts-with(@class,"content__list--item--main")]/p[2]/a[3]/text()').extract_first()
            info_item['title'] = title
            info_item["information1"] = informaton1
            info_item["information2"] = informaton2
            info_item["information3"] = informaton3
            yield info_item


        base_url = "http://%s.lianjia.com/zufang//"
        for city in ["sh", "gz", "gz", "qd" ,"hz", "yt"]:
            full_url = base_url % city
            yield scrapy.Request(url=full_url, callback=self.parse)

