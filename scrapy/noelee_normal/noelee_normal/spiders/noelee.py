# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NoeleeSpider(CrawlSpider):
    name = 'noelee'
    allowed_domains = ['rarbgprx.org']
    start_urls = ['https://rarbgprx.org/torrents.php?search=%22Strapless+Dildo%22']

    rules = (
        Rule(LinkExtractor(allow=r'page='), follow=True),
        Rule(LinkExtractor(restrict_xpaths="//tr[@class='lista2']"), follow=False, callback='parse_item_detail'),
    )

    def parse_item_detail(self, response):
        item = dict(
            item_name=response.xpath("//h1/text()").extract_first(),
            poster=response.xpath("//td[text()=' Poster:']/../td[2]/img/@src").extract_first(),
            Screenshots=response.xpath("//td[text()='Screenshots:']/a/@href").extract_first()
        )
        print(item)
        yield scrapy.Request(
            item['Screenshots'],
            callback=self.parse_Screenshots,
            meta={'item': item}
        )
        yield scrapy.Request(
            item['poster'],
            callback=self.save_img,
            meta={'item': item, 'img_num': '1'}
        )

    def parse_Screenshots(self, response):
        item = response.meta['item']
        item['Screenshots'] = response.xpath("//img/@src").extract_first()
        yield scrapy.Request(
            item['Screenshots'],
            callback=self.save_img,
            meta={'item': item, 'img_num': '2'}
        )

    def save_img(self, response):
        item = response.meta['item']
        with open('./public/' + item['item_name'] + '-' + item['img_num'] + response.url.split('.')[-1], 'wb') as f:
            f.write(response.body)
