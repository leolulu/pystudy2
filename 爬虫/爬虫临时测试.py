import requests
import re
import json

header={
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "cookie": "__cfduid=d70490e4ee6a0bef07b2d00713505d6931522577045; _ga=GA1.3.1025708195.1522577046; _ga=GA1.2.2124586983.1522577050; _gid=GA1.2.431728190.1537370028; _gid=GA1.3.431728190.1537370028; Hm_lvt_ba7c84ce230944c13900faeba642b2b4=1536666453,1537110317,1537370034,1537370545; Hm_lpvt_ba7c84ce230944c13900faeba642b2b4=1537371149"
}

proxies ={
    "http": "socks5://127.0.0.1:1080",
    'https': 'socks5://127.0.0.1:1080'
}

r = requests.get('http://boards.4chan.org/s/catalog',headers=header,proxies = proxies)

rer = re.findall('var catalog =(.*?);var style_group', r.content.decode())

j1 = json.loads(rer[0])['threads']


for i in j1:
    print(
        "http://boards.4chan.org/s/thread/"+i
        # (j1[i]['sub']+j1[i]['teaser'])[:40:]
    )