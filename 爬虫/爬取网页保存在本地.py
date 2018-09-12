import requests

r =  requests.get('http://konachan.net/')


with open('./public/a.html','w',encoding='utf-8') as f:
    f.write(
        r.content.decode('utf-8'),
    )