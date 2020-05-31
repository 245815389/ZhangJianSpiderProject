# -*- coding: utf-8 -*-
import scrapy
from .. items import FangyuanItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['http://bj.lianjia.com/zufang//']
    custom_settings = {
        'ITEM_PIPELINES' : {
            'fangyuan.pipelines.FangyuanPipeline': 300,
            'fangyuan.pipelines.MonPipeline': 300,
        }
    }

    def parse(self, response):
        item = FangyuanItem()
        data1 = response.xpath(
            '//div[starts-with(@class,"content__article")]/p[@class="content__title"]/span/text()').extract_first()
        city_data = response.xpath(
            '//div[starts-with(@class,"content__article")]/p[@class="content__title"]/a/text()').extract_first()
        item["data1"] = data1  # 租房数量
        item["city"] = city_data
        yield item

        # div_list = response.xpath('//div[@class="content__list--item"]')
        # for div in div_list:
        #     info_item = info_FangyuanItem()
        #     title = div.xpath('./div[starts-with(@class,"content__list--item--main")]/p[1]/a/text()').extract_first()
        #     informaton1 = div.xpath('./div[starts-with(@class,"content__list--item--main")]/p[2]/a[1]/text()').extract_first()
        #     informaton2 = div.xpath('./div[starts-with(@class,"content__list--item--main")]/p[2]/a[2]/text()').extract_first()
        #     informaton3 = div.xpath('./div[starts-with(@class,"content__list--item--main")]/p[2]/a[3]/text()').extract_first()
        #     info_item['title'] = title
        #     info_item["information1"] = informaton1
        #     info_item["information2"] = informaton2
        #     info_item["information3"] = informaton3
        #     yield info_item


        base_url = "http://%s.lianjia.com/zufang//"
        for city in ["sh", "gz", "gz", "qd" ,"hz", "yt"]:
            full_url = base_url % city
            yield scrapy.Request(url=full_url, callback=self.parse)

