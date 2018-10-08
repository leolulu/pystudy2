# -*- coding: utf-8 -*-
import scrapy


class KonachanSpider(scrapy.Spider):
    name = 'konachan'
    allowed_domains = ['konachan.com','konachan.net']
    start_urls = ['http://konachan.com/post?tags=girls_frontline']

    page_num = 1

    def parse(self, response):
        img_list = response.xpath("//ul[@id='post-list-posts']/li/a/@href").extract()
        for img in img_list:
            item = {}
            item['page_num'] = KonachanSpider.page_num
            item['pic_name'] = img.split('/')[-1].replace('%20','_').replace('Konachan.com_-_','')
            item['url'] = img
            yield scrapy.Request(
                item['url'],
                callback=self.img_parse,
                meta={'item':item}
            )
        
        next_page_url = response.xpath("//a[text()='Next →']/@href").extract_first()
        if next_page_url is not None:
            KonachanSpider.page_num += 1
            next_page_url = "http://konachan.net" + next_page_url
            yield scrapy.Request(
                next_page_url,
                callback=self.parse
            )

    def img_parse(self,response):
        item = response.meta['item']
        item['img_data'] = response.body
        yield item