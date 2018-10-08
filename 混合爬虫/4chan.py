from selenium import webdriver
from lxml import etree
import requests

browser = webdriver.Chrome()

browser.get("http://boards.4chan.org/h/catalog")

with open('response.html', 'w', encoding='utf-8') as f:
    f.write(browser.page_source)

browser.quit()