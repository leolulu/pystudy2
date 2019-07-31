import requests
from lxml import etree
import time
import os
from retrying import retry
from concurrent.futures import ThreadPoolExecutor
import threading

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
proxies = {
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}

try:
    os.makedirs('./public/yandere/')
except:
    pass

next_url_list = [
    'https://yande.re/post?tags=tentacles'
]

pic_url_list = []
length_of_pic_left = 0
# //div[@class='pagination']/a[last()-1]/text()
# https://yande.re/post?tags=pantyhose&page=613
lock = threading.Lock()
page_num = 1


@retry(wait_exponential_multiplier=1000, wait_exponential_max=60000)
def processing(page_url):
    global page_num
    print(page_url)
    r = requests.get(page_url, proxies=proxies, headers=headers).content
    img_urls = etree.HTML(r).xpath("//ul[@id='post-list-posts']/li/a/@href")
    with lock:
        pic_url_list.extend(img_urls)
        print('current Page.{},length of pic list is {}.'.format(page_num, len(pic_url_list)))
        page_num += 1
# @retry(wait_exponential_multiplier=1000, wait_exponential_max=60000)
# def processing(next_url):
#     page_num = 1
#     # next_url = 'https://yande.re/post?tags=g41_%28girls_frontline%29'
#     while next_url is not None:
#         r = requests.get(next_url, proxies=proxies, headers=headers).content
#         img_urls = etree.HTML(r).xpath("//ul[@id='post-list-posts']/li/a/@href")
#         pic_url_list.extend(img_urls)
#         next_url = 'https://yande.re' + etree.HTML(r).xpath("//a[@class='next_page']/@href")[0] if len(etree.HTML(r).xpath("//a[@class='next_page']/@href")) > 0 else None
#         print('current Page.{},length of pic list is {}.'.format(page_num, len(pic_url_list)))
#         page_num += 1


@retry(wait_exponential_multiplier=1000, wait_exponential_max=60000)
def downloadPic(img_url):
    global length_of_pic_left
    # print('downloading: ', 'page:{} '.format(str(page_num)), img_url)
    file_name = "./public/yandere/"+img_url.split('/')[-1].replace('%20', '_').replace('yande.re_', '')
    if os.path.exists(file_name):
        length_of_pic_left -= 1
        print(length_of_pic_left,'exsits.')
        return
    content = requests.get(img_url, timeout=600, proxies=None, headers=headers).content
    with open(file_name, 'wb') as f:
        # try:
        #     f.write(requests.get(img_url, timeout=600, proxies=proxies, headers=headers).content)
        #     length_of_pic_left -= 1
        #     print('{}pics left to download.'.format(length_of_pic_left))
        # except Exception as e:
        #     print(e)
        #     time.sleep(60)
        f.write(content)
        length_of_pic_left -= 1
        print('{}pics left to download.'.format(length_of_pic_left))


for url in next_url_list:
    r = requests.get(url, proxies=proxies, headers=headers).content
    catagray_page_count = int(etree.HTML(r).xpath("//div[@class='pagination']/a[last()-1]/text()")[0])
    # catagray_page_count = 20 #TEMP!!!TEMP!!!TEMP!!!TEMP!!!TEMP!!!TEMP!!!TEMP!!!TEMP!!!TEMP!!!TEMP!!!TEMP!!!TEMP!!!TEMP!!!
    with ThreadPoolExecutor(max_workers=16) as excutor:
        # for url in [url+'&page='+str(i+1) for i in range(catagray_page_count)]:
        #     excutor.submit(processing,url)
        excutor.map(processing, [url+'&page='+str(i+1) for i in range(catagray_page_count)])
print('total list crawl finish.')

length_of_pic_left = len(pic_url_list)

with ThreadPoolExecutor(max_workers=5) as excutor:
    excutor.map(downloadPic, pic_url_list)
