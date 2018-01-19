import requests
import pandas as pd
from bs4 import BeautifulSoup

r = requests.get('http://www.yangtse.com/app/health/')
soup = BeautifulSoup(r.text,'html.parser')
newsitems = soup.find_all('div',attrs={'class':'box'})



articles = []
x=0
z=0
y=2
w=0

#
# for x in range(0,20):
#     a=0
#     r = requests.get('http://www.yangtse.com/app/health/')
#     soup = BeautifulSoup(r.text,'html.parser')
#     newsitems = soup.find_all('div',attrs={'class':'box'})
#     curr_newsitem = newsitems[a]
#     title=curr_newsitem.find('div',{'class':'box-text-title'}).text
#     link=curr_newsitem.find('a')['href']
#     date=curr_newsitem.find('div',{'class':'box-text-time'}).text
#     articles.append((title,link,date))
#     x+=1
#     a+=1
# for x in range(21,40):
#     b=0
#     r = requests.get('http://www.yangtse.com/app/health/index_2.html')
#     soup = BeautifulSoup(r.text,'html.parser')
#     newsitems = soup.find_all('div',attrs={'class':'box'})
#     curr_newsitem = newsitems[b]
#     title=curr_newsitem.find('div',{'class':'box-text-title'}).text
#     link=curr_newsitem.find('a')['href']
#     date=curr_newsitem.find('div',{'class':'box-text-time'}).text
#     articles.append((title,link,date))
#     x+=1
#     b+=1
# for x in range(41,60):
#     c=0
#     r = requests.get('http://www.yangtse.com/app/health/index_3.html')
#     soup = BeautifulSoup(r.text,'html.parser')
#     newsitems = soup.find_all('div',attrs={'class':'box'})
#     curr_newsitem = newsitems[c]
#     title=curr_newsitem.find('div',{'class':'box-text-title'}).text
#     link=curr_newsitem.find('a')['href']
#     date=curr_newsitem.find('div',{'class':'box-text-time'}).text
#     articles.append((title,link,date))
#     x+=1
#     c+=1
# for x in range(61,80):
#     d=0
#     r = requests.get('http://www.yangtse.com/app/health/index_4.html')
#     soup = BeautifulSoup(r.text,'html.parser')
#     newsitems = soup.find_all('div',attrs={'class':'box'})
#     curr_newsitem = newsitems[d]
#     title=curr_newsitem.find('div',{'class':'box-text-title'}).text
#     link=curr_newsitem.find('a')['href']
#     date=curr_newsitem.find('div',{'class':'box-text-time'}).text
#     articles.append((title,link,date))
#     d+=1
# for x in range(81,100):
#     e=0
#     r = requests.get('http://www.yangtse.com/app/health/index_5.html')
#     soup = BeautifulSoup(r.text,'html.parser')
#     newsitems = soup.find_all('div',attrs={'class':'box'})
#     curr_newsitem = newsitems[x]
#     title=curr_newsitem.find('div',{'class':'box-text-title'}).text
#     link=curr_newsitem.find('a')['href']
#     date=curr_newsitem.find('div',{'class':'box-text-time'}).text
#     articles.append((title,link,date))
#     x+=1
#     print(articles)

for z in range(0,20): #handle statically
    r = requests.get('http://www.yangtse.com/app/health/')
    soup = BeautifulSoup(r.text,'html.parser')
    newsitems = soup.find_all('div',attrs={'class':'box'})
    curr_newsitem = newsitems[x]
    title=curr_newsitem.find('div',{'class':'box-text-title'}).text
    link=curr_newsitem.find('a')['href']
    date=curr_newsitem.find('div',{'class':'box-text-time'}).text
    articles.append((title,link,date))
    z+=1
    x+=1
for z in range(21,101):
    stry=str(y)  #handle somewhat dynamically
    r = requests.get('http://www.yangtse.com/app/health/index_'+ stry + '.html')
    soup = BeautifulSoup(r.text,'html.parser')
    newsitems = soup.find_all('div',attrs={'class':'box'})
    curr_newsitem = newsitems[w]
    title=curr_newsitem.find('div',{'class':'box-text-title'}).text
    link=curr_newsitem.find('a')['href']
    date=curr_newsitem.find('div',{'class':'box-text-time'}).text
    articles.append((title,link,date))
    z+=1
    w+=1
    if w%20==0:
        w-=20
        y+=1
        z+=1



print(len(articles))
