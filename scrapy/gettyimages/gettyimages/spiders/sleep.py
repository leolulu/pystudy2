# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib import parse


class SleepSpider(CrawlSpider):
    name = 'sleep'
    allowed_domains = ['gettyimages.com']
    # start_urls = ['https://www.gettyimages.com/']
    start_urls = ['https://www.gettyimages.com/photos/romantic-young-couple-sleeping-in-bed?mediatype=photography&page=2&phrase=romantic%20young%20couple%20sleeping%20in%20bed&sort=mostpopular']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='next']"), follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='previous']"), follow=True),
        Rule(LinkExtractor(restrict_xpaths="//section[@class='search-results']//article[@class='mosaic-asset']//a"), callback='parse_item', follow=False),

    )

    def start_requests(self):
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            dont_filter=True
        )

    def parse_item(self, response):
        img_url = response.xpath("//div[@class='zoom-wrapper']/img/@src").extract_first()
        print(
            img_url
        )
