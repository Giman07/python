import selenium
from selenium import webdriver
import re
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# 단어 찾아 추천 누르기.
class vote:
    def __init__(self,url,headers,driver,word,xpath_vote,a,class_title):
        self.url= url
        self.headers = headers
        self.driver = driver
        self.word = word
        self.xpath_vote = xpath_vote
        self.a = a
        self.class_title = class_title
        
    def parsing_web(self):
        html=requests.get(self.url, headers = self.headers).text
        bsObject = BeautifulSoup(html, 'html.parser')
        return bsObject
    
    def click_vote(self):
        bs=self.parsing_web()
        my_web = bs.find_all(self.a,class_=self.class_title)   #사이트특성
        self.driver.implicitly_wait(1)
        my_titles = [each_line.get_text().strip() for each_line in my_web[:40]]
        my_links = [each_line.get('href') for each_line in my_web[:40]]
        
        for i in range(40):
             if self.word in my_titles[i]:  # 입력받은 w가 my_titles에 있으면
                 elem=my_links[i]
                 time.sleep(1)
                 self.driver.get(elem)       #click
                 time.sleep(1)      #추천버튼 찾아서 누르기
                 self.driver.find_element_by_xpath(self.xpath_vote).click()
                 print('눌렀음')
                                    #5초 기다린후  alert 종료
                 try:
                      WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
                      alert = self.driver.switch_to.alert
                      alert = self.driver.switch_to.alert
                      alert.accept()
                      time.sleep(1)
                      self.driver.back()
                      time.sleep(1)
                 except TimeoutException:
                     time.sleep(1)
                     self.driver.back()
