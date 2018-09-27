import requests
from lxml import etree
import time

page_num = 1
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
proxies = {
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}
next_url = 'https://yande.re/post?tags=girls_frontline'

while next_url is not None:
    r = requests.get(next_url,proxies=proxies).content
    img_urls = etree.HTML(r).xpath("//ul[@id='post-list-posts']/li/a/@href")
    next_url = 'https://yande.re' + etree.HTML(r).xpath("//a[@class='next_page']/@href")[0] if len(etree.HTML(r).xpath("//a[@class='next_page']/@href")) > 0 else None
    for img in img_urls:
        print('downloading: ','page:'+str(page_num),img)
        with open("./public/yandere/"+img.split('/')[-1].replace('%20','_').replace('yande.re_',''),'wb') as f:
            try:
                f.write(requests.get(img,timeout=600).content)
            except Exception as e:
                print(e)
                time.sleep(60)
    page_num += 1
    
