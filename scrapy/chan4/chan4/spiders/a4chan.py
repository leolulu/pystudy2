# -*- coding: utf-8 -*-
import scrapy
import json
import time


class A4chanSpider(scrapy.Spider):
    name = '4chan'
    allowed_domains = ['4chan.org']
    start_urls = ['https://boards.4chan.org/fa/catalog']



    def parse(self, response):   
        yield {
            "requestBody":response.body,
            'thread_js':response.selector.re('var catalog =(.*?);var style_group')[0]
            }     
        
        


