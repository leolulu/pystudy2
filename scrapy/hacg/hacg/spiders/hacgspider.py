# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HacgspiderSpider(CrawlSpider):
    name = 'hacgspider'
    allowed_domains = ['liuli.eu']
    start_urls = ['http://www.liuli.eu/wp/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[text()='>']"), follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@id='content']/article//h1/a"), callback='parse_every_article', follow=False),
    )

    def parse_every_article(self, response):
        article_info = {}
        article_info['page_url'] = response.url
        article_info['title'] = response.xpath("//header/h1/text()").extract_first()
        article_info['public_time'] = response.xpath("//header/div[@class='entry-meta']/a//text()").extract_first()
        article_info['author'] = response.xpath("//header/div[@class='entry-meta']/span[@class='by-author']/span[2]//text()").extract_first()
        article_info['rating'] = response.xpath("//div[@class='entry-header']/div//strong[last()]/text()").extract_first()
        yield article_info