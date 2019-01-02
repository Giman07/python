import selenium
from selenium import webdriver
import re
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 단어 검색 후 추천 누르고 뒤로 가서 다음 검색
def word(url,w,driver):
    # url 열고 파싱
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    html=requests.get(url, headers = headers).text
    bsObject = BeautifulSoup(html, 'html.parser')
    # 글 제목 따오기
    my_titles = bsObject.find_all('span',class_='ed title-link') 
    my_titles = [each_line.get_text().strip() for each_line in my_titles[:20]]
    for i in range(20):
        if w in my_titles[i]: # 입력받은 w가 my_titles에 있으면
            elem=driver.find_element_by_partial_link_text(my_titles[i])
            elem.click() # 그 이름을 가지고 있는 곳 가서 클릭
            time.sleep(2)
            #추천버튼 찾아서 누르기
            driver.find_element_by_xpath('//*[@id="article_1"]/div/div/span[1]/button').click()
            print('눌렀음')
            #5초 기다린후  alert 종료
            try:
                WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(5)
                driver.back()
            except TimeoutException:
                time.sleep(5)
                driver.back()
            """
            alert = driver.switch_to_alert()
            time.sleep(5)
            alert.accept()
            """
            #다음 검색을 위해 뒤로가기
            #driver.back()
# main 시작 
# 1. 자동로그인
driver = webdriver.Chrome('C:\chromedriver.exe')
url = 'https://www.dogdrip.net/index.php?mid=dogdrip&page=5'
driver.get(url)
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="navbar"]/div/div[3]/div[2]').click()
time.sleep(3)
elem=driver.find_element_by_xpath('//*[@id="id"]')
elem.send_keys('ghkswns92')
elem=driver.find_element_by_xpath('//*[@id="fo_member_login"]/fieldset/div[2]/input')
elem.send_keys('wkdqkrtnrwp01')
elem.submit()
# 2. 단어 검색
time.sleep(60)
word(url,'본',driver)
