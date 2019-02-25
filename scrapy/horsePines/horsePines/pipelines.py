# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import pymysql
import os


class HorsepinesPipeline(object):
    def __init__(self):
        self.db = pymysql.connect('132.232.0.240', 'yxy', 'test', 'mydb')
        self.cursor = self.db.cursor()

        try:
            os.makedirs('./public/')
        except:
            print('public文件夹已存在!')

    def process_item(self, item, spider):
        # save to db
        sql = "INSERT INTO horse_porn_url(url) VALUES(%s)"
        try:
            self.cursor.execute(sql, (item['page_url']))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print('存入数据库出错了：', e)

        if item['media_name'] is not None:
            media_name = item['media_name']
            media_name = media_name.split('?')[0]
            media_name = str(time.time()) + '.' + media_name.split('.')[-1]
            # print(r'~~~ ', media_name)
            with open('./public/' + media_name, 'wb') as f:
                f.write(item['media_data'])

        return item

    def close_spider(self, spider):
        self.db.close()
