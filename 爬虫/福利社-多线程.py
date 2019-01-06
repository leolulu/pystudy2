import requests
from lxml import etree
import os
from concurrent.futures import ThreadPoolExecutor
from retrying import retry
import threading
import time

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "cookie": "__cfduid=d903e3abeaca2effe91e7b839a96be7211527491373; _ga=GA1.3.1213173136.1527491373; _ga=GA1.2.2716196.1533521826; _gid=GA1.2.2067292582.1537358233; _gid=GA1.3.2067292582.1537358233; Hm_lvt_ba7c84ce230944c13900faeba642b2b4=1537359428,1537361149,1537362700,1537363469; Hm_lpvt_ba7c84ce230944c13900faeba642b2b4=1537363858"
}
proxies = {
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}
base_url = 'http://www.appchina.com'


@retry(wait_exponential_multiplier=1000, wait_exponential_max=60000)
def getArticleList():
    r = requests.get('http://www.appchina.com/column_list/7', proxies=proxies, headers=header)
    total_page_num = etree.HTML(r.content).xpath("//div[@class='discuss_fangye']//li[last()-1]//text()")[0]
    article_urls = ['http://www.appchina.com/column_list/7/{}'.format(i+1) for i in range(int(total_page_num))]
    return article_urls


@retry(wait_exponential_multiplier=1000, wait_exponential_max=60000)
def getDetailPageUrl(every_page):
    r = requests.get(every_page, proxies=proxies, headers=header)
    title = etree.HTML(r.content).xpath("//div[@class='r-txt']/*[position()<2]//text()")
    url = [base_url+i for i in etree.HTML(r.content).xpath("//div[@class='r-txt']/h1/a/@href")]
    detail_page_url.extend(list(zip(url, title)))


@retry(wait_exponential_multiplier=1000, wait_exponential_max=60000)
def picDownloader(url, file_path):
    content = requests.get(url, proxies=proxies, headers=header).content
    with open(file_path, 'wb') as f:
        f.write(content)


@retry(wait_exponential_multiplier=1000, wait_exponential_max=60000)
def getPicUrl(detail_page_info):
    folder_path = './public/福利社/{}'.format(detail_page_info[1])
    r = requests.get(detail_page_info[0], proxies=proxies, headers=header)
    img_urls = etree.HTML(r.content).xpath("//div[@class='article-content']//img/@src")
    try:
        os.makedirs(folder_path)
    except Exception as e:
        print(detail_page_info[1], e)
    with ThreadPoolExecutor(6) as excutor:
        for url in img_urls:
            excutor.submit(picDownloader, url, os.path.join(folder_path, url.split('/')[-1]))


article_page_urls = getArticleList()

detail_page_url = []
with ThreadPoolExecutor(32) as excutor:
    excutor.map(getDetailPageUrl, article_page_urls)

with ThreadPoolExecutor(6) as excutor:
    excutor.map(getPicUrl, detail_page_url)
