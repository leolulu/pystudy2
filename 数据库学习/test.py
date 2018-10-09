from urllib import parse

a = "http://www.tianqihoubao.com/lishi/chengdu.html"
b = "/lishi/chengdu/month/201803.html"

c = parse.urljoin(a,b)

print(c)