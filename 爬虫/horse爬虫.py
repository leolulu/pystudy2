import requests
from lxml import etree
import re

header = {
    "Referer": "https://zooredtube.com/zoo/horse-porn",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
param = {
    "shs": "zooredtube.com"
}

session = requests.session()
r = session.get('https://zooredtube.com/search/horse/', headers=header)

html = etree.HTML(r.content)

for every_li in html.xpath("//div[@class='content'][1]//ul[@class='thumbs']/li"):
    title = every_li.xpath(".//span/a/text()")[0]
    item_url = 'https://zooredtube.com' + every_li.xpath("./div/a/@href")[0]

    item_result = session.get(item_url)
    video_url = re.findall("video_url: '(.*?)',",item_result.content.decode())[0]
    print(
        session.get(video_url)
    )