import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import fateadm_api
from time import sleep
import random
from PIL import Image
import re
import os
from concurrent.futures import ThreadPoolExecutor
import threading
import pandas as pd

oc = Options()
oc.add_argument('--headless')
oc.add_argument('--disable-gpu')
oc.add_argument('--log-level=3')

lock = threading.Lock()
final_result_list = []
seq_num = 0


def resendCode(browser):
    print('resend code...')
    browser.find_element_by_id('register-mobile-code').click()
    sleep(0.1)
    browser.find_element_by_id('register-mobile-code').click()
    print('resend code over...')


def run(seq_num):

    fapi = fateadm_api.FateadmApi('309294', 'BdM+gl/hibSyJP+uPRTIayvz1T8Po4Kd', '109294', 'w+qA0pvUeRSj+P8zf8ikCkPG95tF8iQX')

    browser_mail = webdriver.Chrome(options=oc)
    browser_tushare = webdriver.Chrome(options=oc)

    browser_mail.set_page_load_timeout(60)

    try:
        browser_tushare.get("https://tushare.pro/register?reg=222170")
        browser_mail.get("http://24mail.chacuo.net/")
    except:
        browser_tushare.quit()
        browser_mail.quit()
        return 'open page timeout'

    browser_tushare.save_screenshot('./images/screenshot-{}.png'.format(seq_num))

    mail_address = browser_mail.find_element_by_id('mail_cur_name').get_attribute('value')
    print(mail_address)

    with lock:
        captcha = browser_tushare.find_element_by_class_name('captcha')
        left = captcha.location['x']
        top = captcha.location['y']
        right = captcha.location['x'] + captcha.size['width']
        bottom = captcha.location['y'] + captcha.size['height']
        im = Image.open('./images/screenshot-{}.png'.format(seq_num))
        im = im.crop((left, top, right, bottom))
        im.save('./images/captcha-{}.png'.format(seq_num))

        print('发送识别请求...')
        rsp = fapi.PredictFromFile('30400', './images/captcha-{}.png'.format(seq_num))

    browser_tushare.find_element_by_id('register-account').send_keys(mail_address)
    browser_tushare.find_element_by_id('register-password').send_keys(''.join(random.sample('zyxwvutsrqponmlkjihgfedcba123456', 8)))
    browser_tushare.find_element_by_id('register-captcha').send_keys(rsp.pred_rsp.value)

    browser_tushare.find_element_by_id('register-mobile-code').click()
    sleep(0.1)
    browser_tushare.find_element_by_id('register-mobile-code').click()

    # register-mobile-code
    # register-send_code

    if browser_tushare.find_element_by_xpath("//label[@class='error']").text == '图形验证码输入错误':
        fapi.Justice(rsp.request_id)
        browser_tushare.quit()
        browser_mail.quit()
        return 'captcha recg incorrect'

    retry_time = 24
    while True:
        try:
            browser_mail.find_element_by_xpath("//*[@id='convertd']/tr/td[position()=2]")
            break
        except NoSuchElementException:
            if retry_time in [5, 11, 17]:
                resendCode(browser_tushare)
            sleep(10)
            print('shit not shown,{} times left to retry!'.format(retry_time))
            retry_time -= 1
            if retry_time < 0:
                browser_tushare.quit()
                browser_mail.quit()
                return 'email unreceives'
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
    global seq_num
    _seq_num = seq_num
    sleep_time = 1 * _seq_num
    seq_num += 1
    print("I'll sleep {}s.".format(sleep_time))
    sleep(sleep_time)
    result_list = []
    for i in range(run_times):
        try:
            result = run(_seq_num)
            result_list.append('第{}次,result:{}.'.format(i+1, result))
        except Exception as e:
            print(e)
    final_result_list.append(result_list)


def superMain():
    for every_file in os.listdir('./images'):
            os.remove(os.path.join('./images', every_file))
    thread_num = 7
    run_times = 7
    with ThreadPoolExecutor(thread_num) as executor:
        executor.map(main, [run_times for i in range(thread_num)])
    print('\nfinal result:\n',pd.value_counts([k.split(':')[-1].replace('.','') for j in final_result_list for k in j]))

if __name__ == '__main__':
    superMain()