from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('http://konachan.net')

browser.find_element_by_id("tags").send_keys("kijin_seija")
browser.find_element_by_id("tags").send_keys(Keys.ENTER)
time.sleep(3)

print(browser.title)

browser.quit()