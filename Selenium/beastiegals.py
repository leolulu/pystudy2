import requests
from lxml import etree
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

oc = Options()
# oc.add_argument('--headless')
# oc.add_argument('--disable-gpu')
oc.add_extension('./2.5.20_0.crx')
browser = webdriver.Chrome(options=oc)

browser.get("https://beastiegals.com/0/")

detail_list = etree.HTML(browser.page_source).xpath("//div[@class='thumbs']/a/@href")
for detail_page in detail_list:
    detail_page = 'https://beastiegals.com' + detail_page
    print(detail_page)
    browser.get(detail_page)
    sleep(3)
    
    video_url = etree.HTML(browser.page_source).xpath("//video/@src")[0]
    print(video_url)

    with open('./public/' + detail_page.split('/')[-1].split('.')[0] + '.mp4', 'wb') as f:
        f.write(
            requests.get(etree.HTML(browser.page_source).xpath("//video/@src")[0]).content
        )


browser.quit()
