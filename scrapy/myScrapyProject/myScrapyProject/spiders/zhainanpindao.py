# -*- coding: utf-8 -*-
import scrapy


class ZhainanpindaoSpider(scrapy.Spider):
    name = 'zhainanpindao'
    allowed_domains = ['zhainanpindao.cc']
    start_urls = ['http://www.zhainanpindao.cc/wumbh/']

    def parse(self, response):
        articles = response.xpath("//article")
        for article in articles:
            item = {}
            item['title'] = article.xpath(".//h3/a/text()").extract_first()
            item['detail'] = article.xpath("//article//p/text()").extract_first()
            yield item

        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(next_url,self.parse)
