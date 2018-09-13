import requests
import json

data = {
    "id": "121",
    "name": "成吉思汗"
}

r = requests.get('http://127.0.0.1:3000/userget', data=data)


thejson = json.loads(
    r.content.decode()
)

for i in thejson:
    print(i['name'])