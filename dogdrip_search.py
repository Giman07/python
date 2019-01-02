import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url = 'https://www.dogdrip.net/index.php?mid=dogdrip&page=1'
html=requests.get(url, headers = headers).text
bsObject = BeautifulSoup(html, 'html.parser')
my_titles = bsObject.find_all('span',class_='ed title-link')
my_titless = [each_line.get_text().strip() for each_line in my_titles[:20]]
my_count = bsObject.find_all('td',class_='ed voteNum text-primary')
my_count = [each_line1.get_text().strip() for each_line1 in my_count[:20]]
my_number = bsObject.find_all('td',class_='ed no text-xxsmall')
my_number = [each_line.get_text().strip() for each_line in my_number[:20]]
my_link = bsObject.find('a')['href']
"""
for i in range(20):
    if "개드" in my_titless[i]:
        print ('여기에 있다!')
        print(my_titles[i])
        print(number)
"""
