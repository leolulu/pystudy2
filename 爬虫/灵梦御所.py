import requests
from lxml import etree
from tqdm import trange


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "cookie": "__cfduid=d2b741cb6598cb90247646f42b54f34691562163447; _ga=GA1.2.688262721.1562163456; voted_18=95%2C94%2C88%2C87; _gid=GA1.2.760004555.1571668849; _gat=1",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "accept-encoding": "gzip, deflate, br"
}
proxies = {
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}


for page_no in trange(485):
    page_url = 'https://blog.reimu.net/page/{}'.format(page_no+1)
    r = requests.get(page_url, proxies=proxies, headers=headers)
    # r = requests.get(page_url, headers=headers)
    html = etree.HTML(r.content)
    for article in html.xpath(r"//article"):
        title_name = article.xpath(r".//h2[@class='entry-title']/a/text()")[0]
        title_url = article.xpath(r".//h2[@class='entry-title']/a/@href")[0]
        posted_on = article.xpath(r"./footer[@class='entry-footer']/span[@class='posted-on']/a/time/text()")[0]
        catagory = '、'.join(article.xpath(r"./footer[@class='entry-footer']/span[@class='cat-links']/a/text()"))
        tag = '、'.join(article.xpath(r"./footer[@class='entry-footer']/span[@class='tags-links']/a/text()"))

        with open('./灵梦御所.txt', 'a', encoding='utf-8') as f:
            f.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(page_no+1, title_name, title_url, posted_on, catagory, tag))
