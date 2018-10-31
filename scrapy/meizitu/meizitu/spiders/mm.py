# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MmSpider(CrawlSpider):
    name = 'mm'
    allowed_domains = ['mmjpg.com', 'shiyunjj.com']
    start_urls = ['http://www.mmjpg.com/tag/xinggan']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[text()='下一页']"), follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='pic']/ul/li/a"),callback='show_page_url', follow=False),
        Rule(LinkExtractor(restrict_xpaths="//a[text()='下一张']",), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        i['title'] = response.xpath("//div[@class='article']/h2/text()").extract_first()
        i['url'] = response.xpath("//div[@class='content']/a/img/@src").extract_first()
        print(i)

    def show_page_url(self,response):
        print(response.url)
    # def parse_start_url(self,response):
    #     i = {}
    #     i['url'] = response.xpath("//div[@class='pic']/ul/li/a/@href").extract()
    #     print(i)
