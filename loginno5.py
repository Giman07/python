import selenium
from selenium import webdriver
import re
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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
        
