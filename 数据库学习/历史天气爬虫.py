import requests
from lxml import etree
from urllib import parse
import re
import pymysql


class TemperatureAnalysis():
    def __init__(self, city_url):
        print("开始处理中...")
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
            "Cookie": "ASP.NET_SessionId=0vgbhjfrpq1eshvabgntdk55; __51cke__=; bdshare_firstime=1538967426374; Hm_lvt_f48cedd6a69101030e93d4ef60f48fd0=1538967426,1538967501; Hm_lvt_ba7c84ce230944c13900faeba642b2b4=1538967426,1538967503; Hm_lpvt_ba7c84ce230944c13900faeba642b2b4=1538967540; Hm_lpvt_f48cedd6a69101030e93d4ef60f48fd0=1538967843; __tins__4560568=%7B%22sid%22%3A%201538967425683%2C%20%22vd%22%3A%204%2C%20%22expires%22%3A%201538969643130%7D; __51laig__=4",
            "Referer": "http://www.tianqihoubao.com/lishi/chengdu.html",
            "Connection": "keep-alive"
        }
        self.city_url = city_url
        # 启动数据库
        self.db = pymysql.connect(host='132.232.0.240', port=3306, user='yxy', password='test', database='mydb')
        self.cursor = self.db.cursor()

    def extract_from_list(self, list):
        """抽取xpath的结果，对空数据返回None"""
        if len(list) == 0:
            return None
        else:
            return list[0]

    def remove_useless_mark(self, str):
        """处理数据，删除缩进回车和空格"""
        return str.replace(' ', '').replace('\r', '').replace('\n', '')

    def process_middleware(self, item):
        """把extract_from_list和remove_useless_mark合二为一"""
        return self.remove_useless_mark(self.extract_from_list(item))

    def page_parser(self, city_url):
        """从城市首页解析每一个月的地址"""
        r = requests.get(city_url, headers=self.header)
        html = etree.HTML(r.content.decode('gbk'))
        url_list = html.xpath("//div[@id='content']//ul/li/a/@href")
        return [parse.urljoin(r.url, i) for i in url_list]

    def daily_temp_parse(self, page_url):
        """在每月的界面解析每天的数据"""
        daily_info = []
        r = requests.get(page_url, headers=self.header)
        html = etree.HTML(r.content.decode('gbk'))
        rows = html.xpath("//table//tr[position()>1]")
        for row in rows:
            row_info = {}
            row_info['date'] = self.process_middleware(row.xpath("./td[1]/a/text()"))
            row_info['date'] = re.sub("年|月", '-', row_info['date']).replace('日', '')
            row_info['weather'] = self.process_middleware(row.xpath("./td[2]/text()"))
            temperature = self.process_middleware(row.xpath("./td[3]/text()")).replace('℃', '')
            row_info['temperature_high'] = temperature.split('/')[0]
            row_info['temperature_low'] = temperature.split('/')[1]
            row_info['wind'] = self.process_middleware(row.xpath("./td[4]/text()"))
            daily_info.append(row_info)

        return daily_info

    def item_pipeline(self, data):
        """插入数据库"""
        sql = 'insert into weather_scrapy values(%s,%s,%s,%s,%s)'
        params = (
            data['date'],
            data['weather'],
            data['temperature_high'],
            data['temperature_low'],
            data['wind']
        )
        # 操作数据库
        try:
            self.cursor.execute(sql, params)
            self.db.commit()
        except Exception as e:
            print(e)

    def run(self):
        for every_url in self.page_parser(self.city_url):
            for daily_data in self.daily_temp_parse(every_url):
                self.item_pipeline(daily_data)
        # 关闭数据库
        self.db.close()
        print("处理结束！")

t1 = TemperatureAnalysis("http://www.tianqihoubao.com/lishi/chengdu.html")
t1.run()
