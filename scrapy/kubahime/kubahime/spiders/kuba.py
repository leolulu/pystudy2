# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class KubaSpider(CrawlSpider):
    name = 'kuba'
    allowed_domains = ['gelbooru.com']
    start_urls = ['https://gelbooru.com/index.php?page=post&s=list&tags=bowsette']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[text()='›']"), follow=True,callback='show_page_url'),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='thumbnail-preview']//a"), callback='parse_item', follow=False),
    )

    def show_page_url(self,response):
        print(response.url)

    def parse_item(self, response):
        yield scrapy.Request(
            response.xpath("//img[@id='image']/@src").extract_first(),
            callback=self.get_image
        )
    
    def get_image(self,response):
        yield {
            'img_name':response.url.split('/')[-1],
            'img_data':response.body
        }
