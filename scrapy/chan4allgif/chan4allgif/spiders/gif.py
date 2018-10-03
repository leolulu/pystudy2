# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import os


class GifSpider(CrawlSpider):
    name = 'gif'
    allowed_domains = ['beastforum.com']
    start_urls = ['https://www.beastforum.com/showtopic-123113.html']
    # allowed_domains = ['liuli.eu']
    # start_urls = ['http://www.liuli.eu/wp/']
    img_type = 'jpg'
    img_num = 1

    rules = (
        Rule(LinkExtractor(), follow=True),
        Rule(LinkExtractor(allow=r".*\.{}".format(img_type), tags=('img'), attrs=('src'), deny_extensions=()), callback='parse_gif', follow=False),
    )

    def parse_start_url(self, response):
        with open('./start.html','w',encoding='utf-8') as f:
            f.write(response.body.decode())

        self.path_name = './public/{}/'.format(GifSpider.img_type)
        try:
            os.makedirs(self.path_name)
        except:
            print('文件夹已存在')

    # def parse_gif(self, response):
    #     for img_i in response.xpath("//img/@src").extract():
    #         if img_i.split('.')[-1] == self.img_type:
    #             print(
    #                 response.url,img_i
    #             )
    #             yield scrapy.Request(
    #                 img_i,
    #                 callback=self.save_img
    #             )
    def parse_gif(self, response):
        print(
            response.url
        )
        with open(self.path_name + str(GifSpider.img_num) +response.url.split('/')[-1], 'wb') as f:
            f.write(response.body)
        GifSpider.img_num += 1

    # def save_img(self, response):
    #     with open(self.path_name + response.url.split('/')[-1], 'wb') as f:
    #         f.write(response.body)
