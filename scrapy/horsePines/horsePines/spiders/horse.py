# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class HorseSpider(CrawlSpider):
    name = 'horse'
    # allowed_domains = ['seehorsepenis.com','mediacnt.com']
    start_urls = ['http://www.horsecockloving.com/', 'http://www.girl-horse-fuck.gdn', 'http://www.horse-zoo.com/', 'http://www.horseandgirl.com/', 'http://www.horsesexgirl.net/',
                  'http://www.horsezoosex.net', 'http://www.lovehorse.top', 'http://www.porn-horse.com/', 'http://www.horsesandteengirls.com'
                  ]

    rules = (
        Rule(LinkExtractor(allow=r".*horse.*|.*media.*", deny=r".*dog.*"), callback='parse_a',  follow=True),
        # Rule(LinkExtractor(restrict_xpaths="//div[@class='hidePreview']/a"), callback='parse_a', follow=False),
    )

    def parse_a(self, response):
        # print('>>> ', response.url)
        mp4_list = re.findall(r"(http.*?\.(mp4|flv|avi|mkv|webm))", response.text)
        if len(mp4_list) > 0:
            for media_url_tuple in mp4_list:
                media_url = media_url_tuple[0]
                if media_url.find('"') == -1:
                    # print(media_url, '<========')
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
