# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TestSpider(CrawlSpider):
    name = 'test'
    allowed_domains = ['gelbooru.com']
    start_urls = ['https://gelbooru.com/index.php?page=post&s=view&id=4429605']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_start_url(self, response):
        print('fuckfuckfuckfuckfuckfuckfuckfuckfuckfuck')
        print(
            response.xpath("//meta[@property='og:image']/@content").extract()
        )
        with open('./shit.html','w',encoding='utf-8') as f:
            f.write(response.body.decode())
