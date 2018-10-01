# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import os


class GeSpider(CrawlSpider):
    name = 'ge'
    allowed_domains = ['gelbooru.com']
    start_urls = ['https://gelbooru.com/index.php?page=post&s=list&tags=princess_king_boo']
    img_num = 1

    rules = (
        Rule(LinkExtractor(restrict_xpaths = "//div[@class='pagination']/a"), follow=True),
        Rule(LinkExtractor(restrict_xpaths = "//div[@class='thumbnail-preview']/span/a"), follow=False,callback='parse_preview'),
    )

    def parse_start_url(self,response):
        self.catagray = response.xpath("//input[@id='tags-search']/@value").extract_first()
        os.makedirs('./public/'+self.catagray)

        

    def parse_preview(self, response):
        yield scrapy.Request(
            response.xpath("//img[@id='image']/@src").extract_first(),
            callback = self.parse_img
        )

    def parse_img(self,response):
        yield {
            'img_name' : str(GeSpider.img_num) + '.' +response.url.split('/')[-1].split('.')[-1],
            'img_data' : response.body,
            'catagray' : self.catagray
        }
        GeSpider.img_num += 1