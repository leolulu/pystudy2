from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('http://konachan.net/')

browser.find_element_by_xpath("//input[@id='tags']").send_keys("kijin_seija")
browser.find_element_by_xpath("//input[@type='submit']").click()

browser.save_screenshot('./konachan.png')

browser.quit()