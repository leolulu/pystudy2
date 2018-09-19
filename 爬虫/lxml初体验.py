from lxml import etree
import requests

ilist = []
pagenum = 0


def deleten(item):
    return item.replace('\n', '')


while pagenum < 500:
    r = requests.get(
        'http://bgm.tv/anime/browser?sort=rank&page={}'.format(pagenum))

    html = etree.HTML(r.content)

    for li_item in html.xpath("//ul[@id='browserItemList']/li"):
        iitem = {}
        iitem['chinese_name'] = li_item.xpath("./div[@class='inner']/h3/a/text()")[
            0] if len(li_item.xpath("./div[@class='inner']/h3/a/text()")) > 0 else None
        iitem['japanese_name'] = li_item.xpath("./div[@class='inner']/h3/small/text()")[
            0] if len(li_item.xpath("./div[@class='inner']/h3/small/text()")) > 0 else None
        iitem['info'] = li_item.xpath("./div[@class='inner']/p[contains(@class,'tip')]/text()")[0].replace(
            '\n', '') if len(li_item.xpath("./div[@class='inner']/p[contains(@class,'tip')]/text()")) > 0 else None
        iitem['score'] = li_item.xpath("./div[@class='inner']/p[@class='rateInfo']/small/text()")[0] if len(
            li_item.xpath("./div[@class='inner']/p[@class='rateInfo']/small/text()")) > 0 else None
        iitem['rate_num'] = li_item.xpath("./div[@class='inner']/p[@class='rateInfo']/span/text()")[0] if len(
            li_item.xpath("./div[@class='inner']/p[@class='rateInfo']/span/text()")) > 0 else None
        ilist.append(iitem)

    print(pagenum)
    pagenum += 1

with open('./result.txt', 'a', encoding='utf-8') as f:
    for i in ilist:
        i = str(i)+'\n'
        f.write(str(i))
