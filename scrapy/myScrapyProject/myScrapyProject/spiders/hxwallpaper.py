# -*- coding: utf-8 -*-
import scrapy


class HxwallpaperSpider(scrapy.Spider):
    name = 'hxwallpaper'
    allowed_domains = ['hexieshe.cn']
    start_urls = ['https://www.hexieshe.cn/664597/']

    def parse(self, response):
        img_url = response.xpath("//p/img/@src").extract()[:-1]
        for i in img_url:
            yield {'url':i}
