# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class HorseSpider(CrawlSpider):
    name = 'horse'
    # allowed_domains = ['seehorsepenis.com','mediacnt.com']
    start_urls = ['https://www.seehorsepenis.com/']

    rules = (
        Rule(LinkExtractor(allow=r".*horse.*|.*media.*"), callback='parse_a',  follow=True),
        # Rule(LinkExtractor(restrict_xpaths="//div[@class='hidePreview']/a"), callback='parse_a', follow=False),
    )

    def parse_a(self, response):
        print('>>> ', response.url)
        pre_url = response.xpath("//div[@class='hidePreview']/a/@href").extract_first()
        if pre_url is not None:
            media_url = re.sub(r'(\d+)(\.mp4)', r'full\2', pre_url)
            print(media_url, '<========')
            yield scrapy.Request(
                media_url,
                callback=self.downloadMedia,
                meta={'page_url': response.url}
            )
        else:
            yield {
                'page_url': response.url,
                'media_name': None,
                'media_data': None
            }

    def downloadMedia(self, response):
        yield {
            'page_url': response.meta['page_url'],
            'media_name': response.url.split('/')[-1],
            'media_data': response.body
        }
