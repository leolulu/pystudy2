import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

next_url = 'http://www.zhainanpindao.cc/wumbh/'

while next_url is not None:
    r = requests.get(next_url)
    html = etree.HTML(r.content)

    articles = html.xpath("//article")
    for article in articles:
        item = {}
        item['title'] = article.xpath(".//h3/a/text()")[0]
        item['detail'] = article.xpath("//article//p/text()")[0]
        print(item)

    next_url = html.xpath("//a[text()='下一页']/@href")[0] if len(
        html.xpath("//a[text()='下一页']/@href")) > 0 else None
