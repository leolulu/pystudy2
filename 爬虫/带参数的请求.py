import requests

params = {
    'wd': 'fuck horse',
    'unkownparam':'u hahah'
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

r = requests.get('https://www.baidu.com/s', headers=headers, params=params)

print(
    r.request.url
)

with open('./public/baidu.html','w',encoding='utf-8') as f:
    f.write(
        r.content.decode('utf-8'),
    )