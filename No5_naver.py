import selenium
from selenium import webdriver
import re
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys
sys.path.append("D:\\python\\No5")
import loginno5
from loginno5 import login_web
import wordsearch
from wordsearch import vote


def main():
    url='https://media.daum.net/'  # 원하는 사이트
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    driver = webdriver.Chrome('C:\chromedriver.exe')
    word = '시' # 원하는 단어를 여기에 입력
    # 사이트의 특성
    xpath_vote = '//*[@id="empathy_pc"]/div/a[1]'
    xpath_loginbutton = '//*[@id="btnMinidaumLogin"]'
    xpath_id = '//*[@id="id"]'
    xpath_password = '//*[@id="inputPwd"]'
    your_id = 'gdasdfqwe'
    your_password = '********'
    a = 'a'
    class_title = 'link_txt'
    #클래스이용
    login=login_web(url,headers,driver,xpath_loginbutton,xpath_id,xpath_password,your_id,your_password)
    time.sleep(5)
    driver.get(url)
    v1=vote(url,headers,driver,word,xpath_vote,a,class_title)
    login.driver_login()
    v1.click_vote()

main()
