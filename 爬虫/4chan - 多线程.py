import requests
from lxml import etree
import os
from concurrent.futures import ThreadPoolExecutor
from retrying import retry
import threading
import re

session = requests.session()
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "cookie": "__cfduid=d903e3abeaca2effe91e7b839a96be7211527491373; _ga=GA1.3.1213173136.1527491373; _ga=GA1.2.2716196.1533521826; _gid=GA1.2.2067292582.1537358233; _gid=GA1.3.2067292582.1537358233; Hm_lvt_ba7c84ce230944c13900faeba642b2b4=1537359428,1537361149,1537362700,1537363469; Hm_lpvt_ba7c84ce230944c13900faeba642b2b4=1537363858"
}
proxies = {
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}
lock = threading.Lock()

r = session.get('http://boards.4chan.org/gif/thread/14513800', headers=header, proxies=proxies)
dir_name = './public/4chan/{}'.format(re.findall(r'<title>(.*?)</title>', r.text)[0].replace('/', ''))
os.makedirs(dir_name)
post = etree.HTML(r.content)

imgs = post.xpath(".//a[@class='fileThumb']/@href")
imgs = ['https:'+i for i in imgs]
f_name = post.xpath(".//div[@class='fileText']/a/text()")
imgs_f_name = zip(imgs, f_name)
total_num = len(imgs)


@retry(wait_exponential_multiplier=1000, wait_exponential_max=60000)
def downloader(item):
    global total_num
    content = session.get(item[0], proxies=proxies, headers=header).content
    with open(os.path.join(dir_name , item[1]), 'wb') as f:
        f.write(content)
    total_num -= 1
    print('{}items left to download.'.format(total_num))


with ThreadPoolExecutor(max_workers=16) as excutor:
    excutor.map(downloader, imgs_f_name)
