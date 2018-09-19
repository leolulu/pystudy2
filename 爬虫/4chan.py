import requests
from lxml import etree
import os
import re
import json

session = requests.session()
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "cookie": "__cfduid=d903e3abeaca2effe91e7b839a96be7211527491373; _ga=GA1.3.1213173136.1527491373; _ga=GA1.2.2716196.1533521826; _gid=GA1.2.2067292582.1537358233; _gid=GA1.3.2067292582.1537358233; Hm_lvt_ba7c84ce230944c13900faeba642b2b4=1537359428,1537361149,1537362700,1537363469; Hm_lpvt_ba7c84ce230944c13900faeba642b2b4=1537363858"
}
proxies = {
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}

base_url = 'http://boards.4chan.org/e'

r = requests.get(base_url+'/catalog',
                 headers=header, proxies=proxies)
rer = re.findall('var catalog =(.*?);var style_group', r.content.decode())
threads_info = json.loads(rer[0])['threads']


for thread in threads_info:
    thread_url = base_url+"/thread/"+thread
    thread_name = (threads_info[thread]['sub'] +
                   threads_info[thread]['teaser'])[:60:].replace(r'/', '').replace(r':', '').replace('\\', '').replace('?', '').strip()
    print('开始处理thread: ', thread_name)

    in_r = session.get(thread_url, proxies=proxies)
    in_html = etree.HTML(in_r.content)

    post_container = in_html.xpath("//div[contains(@class,'postContainer')]")

    try:
        os.makedirs('./public/4chan/'+thread_name)
    except:
        print('新建文件夹失败，跳过该thread.\n')

    try:
        for post in post_container:
            imgs = post.xpath(".//a[@class='fileThumb']/@href")
            print(imgs)
            f_name = post.xpath(".//div[@class='fileText']/a/text()")
            print(f_name)

            if len(imgs) > 0:
                print('downloading: ', f_name[0])
                img = session.get('https:' + imgs[0], proxies=proxies)
                with open('./public/4chan/'+thread_name+'/' + f_name[0], 'wb') as f:
                    f.write(img.content)
    except:
        print('建文件失败，没问题，下一个.\n')
    
