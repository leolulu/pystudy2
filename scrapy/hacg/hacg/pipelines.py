# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xlwt


class HacgPipeline(object):
    def open_spider(self, spider):
        self.workbook = xlwt.Workbook()
        self.shhet1 = self.workbook.add_sheet('数据')
        self.r = 0

    def process_item(self, item, spider):
        # with open('./hacg.txt','a',encoding='utf-8') as f:
        #     f.write(
        #         str(item)+'\n'
        #         )
        c = 0
        for i in item:
            self.shhet1.write(self.r, c, label=item[i])
            c += 1
        self.r += 1
        self.workbook.save('hacg.xls')
        print(self.r)
        return item

    def close_spider(self, spider):
        print('爬完了')
