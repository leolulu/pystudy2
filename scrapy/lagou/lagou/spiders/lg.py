# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import pymysql


class LgSpider(CrawlSpider):
    name = 'lg'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/jobs/mList.html?pageNo=1']
    cookie = "JSESSIONID=ABAAABAAADEAAFID9B87F16B428F5842E439E1F9371A912; _ga=GA1.2.960155728.1539826504; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539826504; user_trace_token=20181018093506-0b1d42eb-d276-11e8-8047-525400f775ce; LGUID=20181018093506-0b1d46bd-d276-11e8-8047-525400f775ce; _gid=GA1.2.1978700427.1539826505; index_location_city=%E6%88%90%E9%83%BD; Hm_lvt_ba7c84ce230944c13900faeba642b2b4=1539826517; X_HTTP_TOKEN=d2cd15264fec5631b630d32b99b81de9; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216684d008b3572-09fbf6c807183d-50432518-2073600-16684d008b44ab%22%2C%22%24device_id%22%3A%2216684d008b3572-09fbf6c807183d-50432518-2073600-16684d008b44ab%22%7D; sajssdk_2015_cross_new_user=1; LG_LOGIN_USER_ID=c60bb4457343b99ba6ba9a321528b441caa2b7c1817e231c7afc980d7f26d84d; _putrc=06E070D28821D676123F89F2B170EADC; login=true; unick=%E8%A2%81%E6%98%9F%E5%AE%87; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=4ed60d62ce27dd1a7e98ad94846f9a4a1bb44526c5468cf90f8483055131ab19; TG-TRACK-CODE=index_checkmore; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539827259; LGRID=20181018094741-ccc726c0-d277-11e8-805a-525400f775ce; Hm_lpvt_ba7c84ce230944c13900faeba642b2b4=1539827259"
    cookie = {i.split('=')[0]: i.split('=')[1] for i in cookie.split('; ')}

    rules = (
        Rule(LinkExtractor(restrict_xpaths=r"//ul[@class='rec_pos']/li/div[@class='rec_pos_l']//a"), callback='parse_item', follow=False),
    )

    def __init__(self, *args, **kwargs):
        super(LgSpider, self).__init__(*args, **kwargs)
        # 启动数据库
        self.db = pymysql.connect(host='132.232.0.240', port=3306, user='yxy', password='test', database='mydb')
        self.cursor = self.db.cursor()

    def start_requests(self):
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=LgSpider.cookie
        )

    def parse_start_url(self, response):
        with open('response.html', 'w', encoding='utf-8') as f:
            f.write(response.body.decode())

    def parse_item(self, response):
        i = {}
        i['job_name'] = response.xpath("//div[@class='position-head']//*[@class='name']/text()").extract_first()
        i['company'] = response.xpath("//div[@class='position-head']//*[@class='company']/text()").extract_first()
        job_request1 = response.xpath("//div[@class='position-head']//dd[@class='job_request']/p[1]/*[1]/text()").extract_first()
        job_request2 = response.xpath("//div[@class='position-head']//dd[@class='job_request']/p[1]/*[2]/text()").extract_first()
        job_request3 = response.xpath("//div[@class='position-head']//dd[@class='job_request']/p[1]/*[3]/text()").extract_first()
        job_request4 = response.xpath("//div[@class='position-head']//dd[@class='job_request']/p[1]/*[4]/text()").extract_first()
        job_request5 = response.xpath("//div[@class='position-head']//dd[@class='job_request']/p[1]/*[5]/text()").extract_first()
        i['job_request'] = job_request1+job_request2+job_request3+job_request4+job_request5
        description = response.xpath("//dd[@class='job_bt']/div//text()").extract()
        description = [re.sub(r"\s", '', i) for i in description]
        i['description'] = '\n'.join([i for i in description if i != ''])
        yield i
