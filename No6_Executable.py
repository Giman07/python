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
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    driver = webdriver.Chrome('C:\chromedriver.exe')
    
    # 사이트의 특성
    print('사이트 주소를 입력하세요.')
    url=input()  # 원하는 사이트
    print('찾고자 하는 단어를 입력하세요.')
    word = input() # 원하는 단어를 여기에 입력
    print('추천버튼의 xpath를 입력해주세요')
    xpath_vote = input()
    print('로그인버튼의 xpath를 입력해주세요')
    xpath_loginbutton = input()
    print('아이디의 xpath를 입력해주세요')
    xpath_id = input()
    print('비밀번호의 xpath를 입력해주세요')
    xpath_password = input()
    print('아이디를 입력해주세요')
    your_id = input()
    print('비밀번호를 입력해주세요')
    your_password = input()
    print('제목의 type을 입력해주세요')
    a = input()
    print('제목의 class를 입력해주세요')
    class_title = input()
    
    #클래스이용
    login=login_web(url,headers,driver,xpath_loginbutton,xpath_id,xpath_password,your_id,your_password)
    time.sleep(5)
    driver.get(url)
    v1=vote(url,headers,driver,word,xpath_vote,a,class_title)
    login.driver_login()
    v1.click_vote()

main()
