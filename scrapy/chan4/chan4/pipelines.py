# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class Chan4Pipeline(object):
    def process_item(self, item, spider):
        json1 = json.loads(item["thread_js"])
        # with open('4chan.html', 'w', encoding='utf-8') as f:
        #     f.write(
        #         item["thread_js"]
        #         )
        return item
