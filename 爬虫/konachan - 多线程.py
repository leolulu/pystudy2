import requests
from lxml import etree
import time
import os
from retrying import retry
from concurrent.futures import ThreadPoolExecutor
import threading
import shutil

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
proxies = {
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}

try:
    os.makedirs('./public/konachan/')
except:
    pass


pic_url_list = []
length_of_pic_left = 0
lock = threading.Lock()
page_num = 1


@retry(wait_exponential_multiplier=1000, wait_exponential_max=60000)
def processing(page_url):
    try:
        global page_num
        print(page_url)
        r = requests.get(page_url, proxies=proxies, headers=headers).content
        with lock:
            img_urls = etree.HTML(r).xpath("//ul[@id='post-list-posts']/li/a/@href")
            pic_url_list.extend(img_urls)
            print('current Page.{},length of pic list is {}.'.format(page_num, len(pic_url_list)))
            page_num += 1
    except Exception as e:
        print(e)


@retry(wait_exponential_multiplier=1000, wait_exponential_max=60000)
def downloadPic(img_url):
    global length_of_pic_left
    path_name ="./public/konachan/"+img_url.split('/')[-1].replace('%20', '_').replace('Konachan.com_-_', '')
    if os.path.exists(path_name) == True:
        os.remove(path_name)
    else:
        content = requests.get(img_url, timeout=600, proxies=proxies, headers=headers).content
        with open(path_name, 'wb') as f:
            f.write(content)
            length_of_pic_left -= 1
            print('{}pics left to download.'.format(length_of_pic_left))


with ThreadPoolExecutor(max_workers=32) as excutor:
    excutor.map(processing, ['http://konachan.com/post?page={}'.format(i+1) for i in range(50)])
print('total list crawl finish.')

length_of_pic_left = len(pic_url_list)

with ThreadPoolExecutor(max_workers=16) as excutor:
    excutor.map(downloadPic, pic_url_list)
