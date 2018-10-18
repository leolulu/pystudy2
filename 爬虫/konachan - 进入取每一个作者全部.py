import requests
from lxml import etree
from urllib import parse


# while page_num < 10:
#     r = session.get('http://konachan.com/post?page={}&tags='.format(page_num), headers=headers, proxies=proxies)
#     html = etree.HTML(r.content)
#     pic_url_list = html.xpath("//ul[@id='post-list-posts']/li/a/@href")
#     for i in pic_url_list:
#         pic_name = i.split('/')[-1].replace('%20', '_').replace('Konachan.com_-_', '')
#         print('downloading: ', page_num, pic_name)
#         with open('./public/konachan/'+pic_name, 'wb') as f:
#             try:
#                 f.write(session.get(i, proxies=proxies).content)
#             except:
#                 pass
#     page_num += 1


class KonachanInner:
    def __init__(self):
        self.except_artist_tag = 'tagme (artist)'
        self.page_num = 1
        self.base_url = 'http://konachan.com/post'
        self.headers = {
            "Cookie": "vote=1; __utmz=20658210.1460984814.55.2.utmcsr=konachan.com|utmccn=(referral)|utmcmd=referral|utmcct=/post/switch; __cfduid=d18af1d27bb5882a6eff521053cb3cc801525011444; tag-script=; country=US; blacklisted_tags=%5B%22%22%5D; konachan.net=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTlhYTcwNjk4YzI4NjdjYWU2YjZhYzg2YTZiOWRlZmQ1BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMTIxZXdwajVzYVRuR0huSWtWWEUrdlJPOE1EMUdCMHdUdG5yMjFXNmNVNm89BjsARg%3D%3D--8a1e71bdae987934cb60ab31c927084b3c5d85c6; __utmc=20658210; Hm_lvt_ba7c84ce230944c13900faeba642b2b4=1536069861,1536796970,1536939737,1537279770; __utma=20658210.97867196.1446035811.1537370253.1537509624.843; __utmt=1; forum_post_last_read_at=%222018-09-21T08%3A00%3A31%2B02%3A00%22; __utmb=20658210.3.10.1537509624; Hm_lpvt_ba7c84ce230944c13900faeba642b2b4=1537509630",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        }
        self.proxies = {
            "http": "socks5://127.0.0.1:1080",
            'https': 'socks5://127.0.0.1:1080'
        }
        self.session = requests.session()
        self.artist_exsist_list = []

    def temp_print(self, item):
        print(item)

    def artist_exsist_func(self, artist_tag_name, func):
        """
        作者排重
        包括方法调用
        """
        if artist_tag_name in self.artist_exsist_list:
            print(artist_tag_name, ': 此artist已存在，跳过')
        elif artist_tag_name == self.except_artist_tag:
            print(artist_tag_name, ': 未知通用artist，跳过')
        else:
            self.artist_exsist_list.append(artist_tag_name)
            func(artist_tag_name)

    def url_compliet(self, url):
        return parse.urljoin(self.base_url, url)

    def parse_url(self, url):
        return self.session.get(url, headers=self.headers, proxies=self.proxies)

    def parse_mainpage(self):
        """
        解析每一个首页
        """
        r = self.parse_url('{}?page={}&tags='.format(self.base_url, self.page_num))
        html = etree.HTML(r.content)
        detail_page_urls = html.xpath("//ul[@id='post-list-posts']/li/div/a/@href")
        detail_page_urls = map(self.url_compliet, detail_page_urls)
        return detail_page_urls

    def parse_detail_page(self, url_list):
        """
        解析详情页
        """
        for url in url_list:
            r = self.parse_url(url)
            html = etree.HTML(r.content)
            artist_name = html.xpath("//li[contains(@class,'tag-type-artist')]/a[2]/text()")[0]
            self.artist_exsist_func(artist_name,self.temp_print)

    def run(self):
        detail_page_urls = self.parse_mainpage() #解析首页，获得每一个详情页的地址
        self.parse_detail_page(detail_page_urls) #解析详情页


k1 = KonachanInner()
k1.run()
