from lxml import etree
import requests

ilist=[]
iitem={}

def deleten(item):
    return item.replace('\n','')

r = requests.get('http://bgm.tv/anime/browser?sort=rank')


html = etree.HTML(r.content)



print(
    html.xpath("//ul[@id='browserItemList']/li")    
)