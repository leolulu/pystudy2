# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class CrawlspiderPipeline(object):
    def process_item(self, item, spider):
        print('saving: ',item['img_name']) 
        with open('./public/'+item['img_name'],'wb') as f:
            f.write(item['img_data'])
        return item
