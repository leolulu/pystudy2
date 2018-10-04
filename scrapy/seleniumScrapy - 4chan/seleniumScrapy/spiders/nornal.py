# -*- coding: utf-8 -*-
import scrapy


class NornalSpider(scrapy.Spider):
    name = 'nornal'
    allowed_domains = ['4chan.org']
    start_urls = ['http://boards.4chan.org/h/catalog']

    def parse(self, response):
        pass

    def start_requests(self,request):
        request = request.replace(meta = {'wahttype': 'img'})