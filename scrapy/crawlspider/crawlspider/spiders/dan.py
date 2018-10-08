# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DanSpider(CrawlSpider):
    name = 'dan'
    allowed_domains = ['donmai.us']
    start_urls = ['https://danbooru.donmai.us/posts?utf8=%E2%9C%93&tags=animated+&ms=1']

    rules = (
        Rule(LinkExtractor(allow=r'/posts/.*?'), callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_xpaths="//a[@rel='next']"), follow=True),
    )

    def parse_item(self, response):
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        img_url = response.xpath("//img[@id='image']/@src").extract_first()
        if img_url is None:
            img_url = response.xpath("//video[@id='image']/@src").extract_first()
        yield scrapy.Request(
            img_url,
            callback=self.image_request,
            meta={'img_url':img_url}
        )

    def image_request(self,response):
        img_url = response.meta['img_url']
        print('downloading: ',img_url) 
        yield {
            'img_name': img_url.split('/')[-1].replace('__',''),
            'img_data' : response.body
        }
