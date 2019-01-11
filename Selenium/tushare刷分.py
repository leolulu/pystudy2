import requests
from lxml import etree
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import random
import fateadm_api
from PIL import Image
import re
from selenium.common.exceptions import NoSuchElementException
import os

oc = Options()
oc.add_argument('--headless')
oc.add_argument('--disable-gpu')


def run():

    for every_file in os.listdir('./images'):
        os.remove(os.path.join('./images', every_file))

    fapi = fateadm_api.FateadmApi('309294', 'BdM+gl/hibSyJP+uPRTIayvz1T8Po4Kd', '109294', 'w+qA0pvUeRSj+P8zf8ikCkPG95tF8iQX')

    browser_tushare = webdriver.Chrome(options=oc)
    browser_mail = webdriver.Chrome(options=oc)

    browser_mail.set_page_load_timeout(20)

    try:
        browser_tushare.get("https://tushare.pro/register?reg=222170")
        browser_mail.get("http://24mail.chacuo.net/")
    except:
        browser_tushare.quit()
        browser_mail.quit()
        return 'open page timeout.'

    browser_tushare.save_screenshot('./images/screenshot.png')

    mail_address = browser_mail.find_element_by_id('mail_cur_name').get_attribute('value')
    print(mail_address)

    captcha = browser_tushare.find_element_by_class_name('captcha')
    left = captcha.location['x']
    top = captcha.location['y']
    right = captcha.location['x'] + captcha.size['width']
    bottom = captcha.location['y'] + captcha.size['height']
    im = Image.open('./images/screenshot.png')
    im = im.crop((left, top, right, bottom))
    im.save('./images/captcha.png')

    print('发送识别请求...')
    rsp = fapi.PredictFromFile('30400', './images/captcha.png')

    browser_tushare.find_element_by_id('register-account').send_keys(mail_address)
    browser_tushare.find_element_by_id('register-password').send_keys(''.join(random.sample('zyxwvutsrqponmlkjihgfedcba123456', 8)))
    browser_tushare.find_element_by_id('register-captcha').send_keys(rsp.pred_rsp.value)

    browser_tushare.find_element_by_id('register-mobile-code').click()
    sleep(1)
    browser_tushare.find_element_by_id('register-mobile-code').click()

    retry_time = 9
    while True:
        try:
            browser_mail.find_element_by_xpath("//*[@id='convertd']/tr/td[position()=2]")
            break
        except NoSuchElementException:
            sleep(10)
            print('shit not shown,{} times left to retry!'.format(retry_time))
            retry_time -= 1
            if retry_time < 0:
                browser_tushare.quit()
                browser_mail.quit()
                return 'err'
    browser_mail.find_element_by_xpath("//*[@id='convertd']/tr/td[position()=2]").click()
    sleep(1)
    i_code = browser_mail.find_element_by_xpath("//div[@id='mailview_data']/div/div").text
    i_code = re.findall("验证码(.+)，", i_code)[0]
    browser_tushare.find_element_by_id('register-verify_code').send_keys(i_code)

    browser_tushare.find_element_by_id('register-btn').click()

    sleep(1)

    browser_tushare.quit()
    browser_mail.quit()
    return 'succ'

def main(run_times):
    result_list = []
    for i in range(run_times):
        try:
            result = run()
            result_list.append('第{}次,result:{}.'.format(i,result))
        except Exception as e:
            print(e)
    print(result_list)

main(run_times=100)