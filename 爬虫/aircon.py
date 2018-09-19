import requests
from lxml import etree

r = requests.get('http://www.alrincon.com/en/blog/mr_hawks_extreme_photography.html')

html = etree.HTML(r.content)
source_url = html.xpath("//div[@class='noticia']//img/@src")

for i in source_url:
    file_name = i.split('/')[-1]
    print('downloading: ', file_name)
    v = requests.get(i)
    with open('./public/4chan/'+file_name, 'wb') as f:
        f.write(v.content)
