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
    def __init__(self,url,headers,driver,word,xpath_vote):
        self.url= url
        self.headers = headers
        self.driver = driver
        self.word = word
        self.xpath_vote = xpath_vote
        
    def parsing_web(self):
        html=requests.get(self.url, headers = self.headers).text
        bsObject = BeautifulSoup(html, 'html.parser')
        return bsObject

    def get_title(self):
        bs=self.parsing_web()
        my_titles = bs.find_all('span',class_='ed title-link')   #사이트특성
        my_titles = [each_line.get_text().strip() for each_line in my_titles[:20]]
        return my_titles

    def click_vote(self):
        my_titles=self.get_title()
        for i in range(20):
             if self.word in my_titles[i]:  # 입력받은 w가 my_titles에 있으면
                 elem=self.driver.find_element_by_partial_link_text(my_titles[i])
                 elem.click()       #click
                 time.sleep(2)      #추천버튼 찾아서 누르기
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
                      time.sleep(4)
                      self.driver.back()
                 except TimeoutException:
                     time.sleep(5)
                     self.driver.back()

class login_web:

    def __init__(self,url,headers,driver,xpath_loginbutton,xpath_id,xpath_password,your_id,your_password):
        self.url = url      
        self.headers = headers
        self.driver = driver
        self.xpath_loginbutton = xpath_loginbutton
        self.xpath_id = xpath_id
        self.xpath_password = xpath_password
        self.your_id = your_id
        self.your_password = your_password
        self.xpath_id = xpath_id
        self.xpath_password = xpath_password

    def driver_login(self):

        self.driver.get(self.url)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath(self.xpath_loginbutton).click() #로그인버튼 xpath
        time.sleep(3)
        elem=self.driver.find_element_by_xpath(self.xpath_id) # 아이디 xpath
        elem.send_keys(self.your_id)
        elem=self.driver.find_element_by_xpath(self.xpath_password)  #비번 xpath
        elem.send_keys(self.your_password)
        elem.submit()
        time.sleep(60)
        
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
   
    #클래스이용
    login=login_web(url,headers,driver,xpath_loginbutton,xpath_id,xpath_password,your_id,your_password)
    v1=vote(url,headers,driver,word,xpath_vote)
    login.driver_login()
    v1.click_vote()


main()
