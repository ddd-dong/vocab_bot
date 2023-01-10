
import requests
import csv
from bs4 import BeautifulSoup



url = "https://crmne0707.pixnet.net/blog/post/298726324-%E9%AB%98%E4%B8%AD%E8%8B%B1%E6%96%877000%E5%96%AE%E5%AD%97-level1%28%E5%AD%B8%E6%B8%AC1%29"
response = requests.get(url)
response.encoding='utf-8'
soup = BeautifulSoup(response.text, "lxml")
txt=soup.find('div',{'id':"article-content-inner"})
a=txt.findChildren("p")
vocab=[]

with open("level.csv", 'w', encoding="utf-8",newline='') as f:
    writer = csv.writer(f)
    writer.writerow({"English", "磁性", "中文"})
    for i in range(6,len(a)):
        if(a[i].string): writer.writerow(a[i].string.split())



