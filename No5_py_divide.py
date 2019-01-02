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
    url='https://www.dogdrip.net/index.php?mid=dogdrip&page=5'  # 원하는 사이트
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    driver = webdriver.Chrome('C:\chromedriver.exe')
    word = 'jpg' # 원하는 단어를 여기에 입력
    # 사이트의 특성
    xpath_vote = '//*[@id="article_1"]/div/div/span[1]/button'
    xpath_loginbutton = '//*[@id="navbar"]/div/div[3]/div[2]'
    xpath_id = '//*[@id="id"]'
    xpath_password = '//*[@id="fo_member_login"]/fieldset/div[2]/input'
    your_id = 'ghkswns92'
    your_password = 'wkdqkrtnrwp01'
    a = 'span'
    class_title = 'ed title-link'
    #클래스이용
    login=login_web(url,headers,driver,xpath_loginbutton,xpath_id,xpath_password,your_id,your_password)
    time.sleep(60)
    v1=vote(url,headers,driver,word,xpath_vote,a,class_title)
    login.driver_login()
    v1.click_vote()


main()
