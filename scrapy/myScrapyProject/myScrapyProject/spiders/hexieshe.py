# -*- coding: utf-8 -*-
import scrapy


class HexiesheSpider(scrapy.Spider):
    name = 'hexieshe'
    allowed_domains = ['hexieshe.cn']
    start_urls = ['https://www.hexieshe.cn/category/wallpaper/']

    def parse(self, response):
        result = response.xpath("//div[@id='primary-home']//div[contains(@class,'content')]//h2//text()").extract()
        for i in result:
            print(i)