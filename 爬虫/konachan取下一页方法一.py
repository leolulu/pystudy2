import requests
from lxml import etree
import os
import re

page_num = 1
headers = {
    "Cookie": "vote=1; __utmz=20658210.1460984814.55.2.utmcsr=konachan.com|utmccn=(referral)|utmcmd=referral|utmcct=/post/switch; __cfduid=d18af1d27bb5882a6eff521053cb3cc801525011444; tag-script=; country=US; blacklisted_tags=%5B%22%22%5D; konachan.net=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTlhYTcwNjk4YzI4NjdjYWU2YjZhYzg2YTZiOWRlZmQ1BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMTIxZXdwajVzYVRuR0huSWtWWEUrdlJPOE1EMUdCMHdUdG5yMjFXNmNVNm89BjsARg%3D%3D--8a1e71bdae987934cb60ab31c927084b3c5d85c6; __utmc=20658210; Hm_lvt_ba7c84ce230944c13900faeba642b2b4=1536069861,1536796970,1536939737,1537279770; __utma=20658210.97867196.1446035811.1537370253.1537509624.843; __utmt=1; forum_post_last_read_at=%222018-09-21T08%3A00%3A31%2B02%3A00%22; __utmb=20658210.3.10.1537509624; Hm_lpvt_ba7c84ce230944c13900faeba642b2b4=1537509630",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
proxies = {
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}
session = requests.session()

next_page_url = 'http://konachan.net/post?tags=sideboob'

dir_name = './public/konachan-{}/'.format(re.findall(r"tags=(.+)", next_page_url)[0])

try:
    os.mkdir(dir_name)
except Exception as e:
    print(e)

while next_page_url is not None:
    r = session.get(next_page_url, headers=headers, proxies=proxies)
    html = etree.HTML(r.content)
    next_page_url = "http://konachan.net"+html.xpath("//a[text()='Next →']/@href")[0] if len(
        html.xpath("//a[text()='Next →']/@href")) > 0 else None

    pic_url_list = html.xpath("//ul[@id='post-list-posts']/li/a/@href")
    for i in pic_url_list:
        pic_name = i.split('/')[-1].replace('%20', '_').replace('Konachan.com_-_', '')
        print('downloading: ', page_num, pic_name)
        with open(dir_name+pic_name, 'wb') as f:
            try:
                f.write(session.get(i, proxies=proxies).content)
            except Exception as e:
                print('下载文件出错：',e)
    page_num += 1
