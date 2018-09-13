import requests


class hjQuery:
    def __init__(self, querystr):
        self.queryurl = 'http://m.youdao.com/translate'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "Referer": "http://fanyi.youdao.com/"
        }
        # self.params = {"smartresult": "dict", "smartresult": "rule"}
        self.data = {
            "inputtext": querystr,
            "type": "ZH_CN2JA"
        }

    def run(self):
        r = requests.post(
            self.queryurl,
            headers=self.headers,
            # params=self.params,
            data= self.data
        )
        print(
            r.request.data
        )


t1 = hjQuery('阔以')
t1.run()
