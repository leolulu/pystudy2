# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GebolurPipeline(object):
    def process_item(self, item, spider):
        with open('./public/' + item['catagray'] +'/' + item['img_name'],'wb') as f:
            f.write(item['img_data'])
        return item
