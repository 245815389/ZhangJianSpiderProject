# -*- coding: utf-8 -*-
import scrapy
from .. items import ZhilianItem

class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['xiaoyuan.zhaopin.com']
    start_urls = ['https://xiaoyuan.zhaopin.com/search/jt=9000300000000&pg=1']

    def parse(self, response):
        div_list = response.xpath('//div[starts-with(@id,"pane-reletive")]/div/div')
        for div in div_list:
            item = ZhilianItem()
            name = div.xpath('.//div[@class="fn-left position"]/text()').extract_first()
            city = div.xpath('.//span[@class="city fn-left"]/text()').extract_first()
            company = div.xpath('.//div[@class="fn-right company"]/text()').extract_first()

            item["name"] = name
            item["city"] = city
            item["company"] = company
            yield item

        base_url = "https://xiaoyuan.zhaopin.com/search/jt=9000300000000&pg=%s"
        for i in range(1, 35):
            full_url = base_url % i
            yield scrapy.Request(url=full_url, callback=self.parse)

