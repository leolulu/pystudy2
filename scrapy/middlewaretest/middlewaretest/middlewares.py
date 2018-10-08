# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

class ProxyMiddleware(object):
    def process_request(self,request,spider):
        request.meta['proxy'] = 'http://127.0.0.1:1080'

class Cookiemiddleware(object):
    def process_request(self,request,spider):
        cookie = "ADNF=a642803401bb64e8eda3f18ee36a7435; __utma=52483902.408065444.1446641088.1492218118.1492355795.289; _ga=GA1.2.408065444.1446641088; user_id=319612; pass_hash=f2ad63ed1614fcddb823dd9fa188feec8fc7c5e6; __cfduid=d6835714e71f517ccc437fddbf831d7191519553182; _gid=GA1.2.1746635511.1538298884; resize-notification=1; resize-original=1; gelcomPoop=1; PHPSESSID=4v1gefdqgh3hokjgc8mr516la7; Hm_lvt_ba7c84ce230944c13900faeba642b2b4=1538298885,1538456222,1538471823,1538477910; _gat_gtag_UA_2246042_1=1; Hm_lpvt_ba7c84ce230944c13900faeba642b2b4=1538481462"
        cookie = { i.split('=')[0]:i.split('=')[1] for i in cookie.split(';') }
        request.cookies = cookie