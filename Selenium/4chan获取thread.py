from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://boards.4chan.org/fa/catalog")

with open('./4chan.html','w',encoding='utf-8') as f:
    f.write(browser.page_source)

browser.quit()

