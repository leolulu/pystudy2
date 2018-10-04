import requests
from lxml import etree
import pymysql


header = {
    "Cookie": "Hm_lvt_60bad21af9c824a4a0530d5dbf4357ca=1538661866; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1538661866; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1538661866; Hm_lvt_ba7c84ce230944c13900faeba642b2b4=1538661866; Hm_lpvt_60bad21af9c824a4a0530d5dbf4357ca=1538661974; Hm_lpvt_f79b64788a4e377c608617fba4c736e2=1538661974; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1538661975; Hm_lpvt_ba7c84ce230944c13900faeba642b2b4=1538661975; v=Ai6Mq4zn-a8pig1LljuQpDa3f4_zL_IpBPOmDVj3mjHsO8Q5wL9COdSD9hUr",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

db = pymysql.connect(host='132.232.0.240', port=3306, user='yxy', password='test', database='mydb')
cursor = db.cursor()


def list_zero_if(list):
    if len(list) == 0:
        return None
    elif len(list) == 2:
        return list[0] + list[1]
    else:
        return list[0]


stock_info = []
stocks = etree.HTML(requests.get("http://data.10jqka.com.cn/ipo/xgsgyzq/", headers=header).content).xpath("//tbody[@class='m_tbd']//tr")
for stock in stocks:
    info = {}
    info['股票代码'] = list_zero_if(stock.xpath("./td[1]/a/text()"))
    info['股票简称'] = list_zero_if(stock.xpath("./td[2]/a/text()"))
    info['申购日期'] = list_zero_if(stock.xpath("./td[11]/text()"))
    info['中签率'] = list_zero_if(stock.xpath("./td[12]/text()"))
    info['发行价格'] = list_zero_if(stock.xpath("./td[8]//text()")).replace('\t', '').replace('\n', '')
    stock_info.append(info)

for i in stock_info:
    print(i)
    sql = '''insert into new_stock values("{}","{}","{}",{},{})'''.format(
        i['股票代码'],
        i['股票简称'],
        i['申购日期'],
        float(i['中签率']),
        float(i['发行价格'])
    )
    cursor.execute(sql)
    db.commit()
