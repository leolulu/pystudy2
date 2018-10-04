# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SeSpider(CrawlSpider):
    name = 'se'
    allowed_domains = ['4chan.org']
    start_urls = ['http://boards.4chan.org/h/catalog']

    rules = (
        Rule(LinkExtractor(allow=r'thread'),  follow=True ),
        Rule(LinkExtractor(tags=('img'), attrs=('src'), deny_extensions=()), callback='parse_item', follow=False,process_request='parse_img_url'),
    )

    def parse_start_url(self, response):
        print('初始请求结束')

    def __init__(self, *a, **kw):
        super(SeSpider, self).__init__(*a, **kw)
        oc = Options()
        oc.add_extension("./2.5.20_0.crx")
        self.browser = webdriver.Chrome(options=oc)

    def closed(self, spider):
        self.browser.quit()

    def parse_item(self, response):
        print(
            '==============>' + response.url
        )
        with open('./public/' + response.url.split('/')[-1], 'wb') as f:
            f.write(response.body)

    def parse_img_url(self, request):
        request = request.replace(meta = {'wahttype': 'img'})
        return request
