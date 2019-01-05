import selenium
from selenium import webdriver
driver.implicitly_wait(1)
driver.find_element_by_xpath('dd').click()
elem=driver.find_element_by_xpath('//*[@id="id"]')
elem.send_keys('ghkswns92')
elem=driver.find_element_by_xpath('//*[@id="fo_member_login"]/fieldset/div[2]/input')
elem.send_keys('wkdqkrtnrwp01')
elem.submit()
