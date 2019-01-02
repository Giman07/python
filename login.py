import selenium
from selenium import webdriver
import re
driver = webdriver.Chrome('C:\chromedriver.exe')
driver.get('https://www.dogdrip.net/index.php?mid=dogdrip&page=2')
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="navbar"]/div/div[3]/div[2]').click()
elem=driver.find_element_by_xpath('//*[@id="id"]')
elem.send_keys('ghkswns92')
elem=driver.find_element_by_xpath('//*[@id="fo_member_login"]/fieldset/div[2]/input')
elem.send_keys('wkdqkrtnrwp01')
elem.submit()
