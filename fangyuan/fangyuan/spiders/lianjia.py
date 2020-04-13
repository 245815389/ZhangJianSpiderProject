# -*- coding: utf-8 -*-
import scrapy
from .. items import FangyuanItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['http://yt.lianjia.com/']

    def parse(self, response):
        li_list = response.xpath('//div[starts-with(@class,"header-wrap")]/div[@class="house-num"]/ul/li')
        item = FangyuanItem()
        try:
            data1 = li_list[0].xpath('./text()').extract_first()
            data2 = li_list[1].xpath('./text()').extract_first()
            data3 = li_list[2].xpath('./text()').extract_first()
            item["data1"] = data1
            item["data2"] = data2
            item["data3"] = data3
            yield item
            print(data1,data2,data3)
        except:
            item["data1"] = data1
            item["data2"] = data2
            yield item
            print(data1,data2)

        # for li in li_list:
        #     item = FangyuanItem()
        #     data = li.xpath('./text()').extract_first()
        #     item["data"] = data
        #     yield item
        base_url = "http://%s.lianjia.com/"
        for city in ["bj", "sh", "gz"]:
            full_url = base_url % city
            yield scrapy.Request(url=full_url, callback=self.parse)