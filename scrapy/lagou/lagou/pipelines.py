# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LagouPipeline(object):
    def process_item(self, item, spider):
        sql = 'insert into lagou_job_info values(%s,%s,%s,%s)'
        params = (
            item['job_name'],
            item['company'],
            item['job_request'],
            item['description']
        )
        # 操作数据库
        try:
            spider.cursor.execute(sql, params)
            spider.db.commit()
        except Exception as e:
            print(e)
        return item
