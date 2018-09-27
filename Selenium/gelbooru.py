from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree

base_url = 'https://gelbooru.com/index.php?page=post&s=list&tags=animated&pid={}'

co = webdriver.ChromeOptions()
co.add_argument('--headless')
co.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=co)

for page_num in range(5):
    browser.get(base_url.format(page_num*42))
    html = etree.HTML(browser.page_source)
    item_urls = html.xpath("//div[@class='contain-push']/div[@class='thumbnail-preview']//a/@href")
    for item in item_urls:
        print(page_num, item)
