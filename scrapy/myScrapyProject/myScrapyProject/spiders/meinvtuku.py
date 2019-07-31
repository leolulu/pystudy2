# -*- coding: utf-8 -*-
import scrapy


class MeinvtukuSpider(scrapy.Spider):
    name = 'meinvtuku'
    allowed_domains = ['win4000.com']
    start_urls = ['http://www.win4000.com/meitu.html']

    def parse(self, response):
        result = response.xpath(r"//div[@class='list_cont list_cont2 w1180']//p/text()").extract()
        for i in result:
            print(i)
