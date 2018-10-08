# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class hxwallpaperpipe(object):
    def process_item(self, item, spider):
        if spider.name == 'hxwallpaper':
            print(item)
        return item


class Zhainanpindaopipe(object):
    def process_item(self, item, spider):
        if spider.name == 'zhainanpindao':
            print(item)
        return item
