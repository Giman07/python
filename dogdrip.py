import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url = 'https://www.dogdrip.net/dogdrip'
html=requests.get(url, headers = headers).text
bsObject = BeautifulSoup(html, 'html.parser')
my_titles = bsObject.find_all('span',class_='ed title-link')
my_titles = [each_line.get_text().strip() for each_line in my_titles[:20]]
my_count = bsObject.find_all('td',class_='ed voteNum text-primary')
my_count = [each_line1.get_text().strip() for each_line1 in my_count[:20]]
for i in range(20):
    print(my_titles[i],end="")
    print(my_count[i])

