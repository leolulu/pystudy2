# -*- coding: utf-8 -*-
import scrapy

proxies = 'http://127.0.0.1:1080'



class KonachanSpider(scrapy.Spider):
    name = 'konachan'
    allowed_domains = ['konachan.net']
    start_urls = ['http://konachan.net/post']

    def parse(self, response):
        print(
            response.body
        )
