import requests
from lxml import etree
import time
import os
from retrying import retry

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
    'https://yande.re/post?tags=fishnets',
    'https://yande.re/post?tags=garter',
    'https://yande.re/post?tags=heels',
    'https://yande.re/post?tags=pantyhose'
]


@retry(wait_fixed=5000, stop_max_attempt_number=7)
def processing(next_url):
    page_num = 1
    # next_url = 'https://yande.re/post?tags=g41_%28girls_frontline%29'
    while next_url is not None:
        r = requests.get(next_url, proxies=proxies, headers=headers).content
        img_urls = etree.HTML(r).xpath("//ul[@id='post-list-posts']/li/a/@href")
        next_url = 'https://yande.re' + etree.HTML(r).xpath("//a[@class='next_page']/@href")[0] if len(etree.HTML(r).xpath("//a[@class='next_page']/@href")) > 0 else None
        for img in img_urls:
            # print('downloading: ', 'page:{} '.format(str(page_num)), img)
            with open("./public/yandere/"+img.split('/')[-1].replace('%20', '_').replace('yande.re_', ''), 'wb') as f:
                try:
                    f.write(requests.get(img, timeout=600, proxies=proxies, headers=headers).content)
                except Exception as e:
                    print(e)
                    time.sleep(60)
        page_num += 1


for url in next_url_list:
    processing(url)
