# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ShitPipeline(object):
    def process_item(self, item, spider):
        print(
            item['page_num'],
            item['url']
        )
        with open('./public/'+item['pic_name'],'wb') as f:
            f.write(item['img_data'])
        return item
