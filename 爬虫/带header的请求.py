import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

r = requests.get('http://konachan.net/', headers=headers)

print(
    r.content.decode()
)
