# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BeastiegalsSpider(CrawlSpider):
    name = 'beastiegals'
    allowed_domains = ['beastiegals.com', 'mediacnt.com']
    start_urls = ['https://beastiegals.com/0/']
    img_num = 1

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='controls']"),  follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='thumbs']/a"),  follow=False, callback='parse_detail'),
    )

    def parse_item(self, response):
        img_list = response.xpath("//img/@src").extract()
        for i in img_list:
            with open('list.txt', 'a', encoding='utf-8') as f:
                f.write(i+'\n')
            yield scrapy.Request(
                url=i,
                callback=self.download_img
            )

    def download_img(self, response):
        print(BeastiegalsSpider.img_num)
        with open('./public/' + str(BeastiegalsSpider.img_num) + '-' + response.url.split('/')[-1], 'wb') as f:
            f.write(response.body)
        BeastiegalsSpider.img_num += 1

    def parse_detail(self, response):
        print(
            response.xpath("//div[@class='hidePreview']/a[1]/@href").extract_first()
        )
        # yield scrapy.Request(
        #     response.xpath("//div[@class='hidePreview']/a[1]/@href").extract_first(),
        #     callback=self.download_video
        # )

    def download_video(self, response):
        with open('./public/' + response.url.split('/')[-1].split('.')[0] + '.mp4', 'wb') as f:
            f.write(response.body)
