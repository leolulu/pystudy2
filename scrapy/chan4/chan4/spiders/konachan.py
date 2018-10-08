# -*- coding: utf-8 -*-
import scrapy


class KonachanSpider(scrapy.Spider):
    name = 'konachan'
    allowed_domains = ['konachan.net']
    start_urls = ['http://konachan.net/post']
    shit='fuckfuck'

    def parse(self, response):
        result = response.xpath("//ul[@id='post-list-posts']/li//a[contains(@class,'directlink')]/@href").extract_first()
        yield {'result':result}
