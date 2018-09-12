import requests

r = requests.get('http://cn.python-requests.org/zh_CN/latest/user/install.html')

r.encoding = 'utf-8'
print(
    r.text
)