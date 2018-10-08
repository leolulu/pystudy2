# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class KubahimePipeline(object):
    pic_num = 1
    def process_item(self, item, spider):
        with open('./public/' + item['img_name'],'wb') as f:
            f.write(item['img_data'])
        print(KubahimePipeline.pic_num)
        KubahimePipeline.pic_num += 1
        return item
