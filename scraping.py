import requests
import pandas as pd
import datetime as dt
from bs4 import BeautifulSoup


# -- vars --
r = requests.get('http://www.yangtse.com/app/health/')
soup = BeautifulSoup(r.text,'html.parser')
newsitems = soup.find_all('div',attrs={'class':'box'})
articles = []
articles_dict = {}
now=str(dt.datetime.now())

def scrape ():
    d = {}
    x=0
    z=0
    y=2
    w=0
    # -- do work --
    for z in range(0,20): #handle statically
        r = requests.get('http://www.yangtse.com/app/health/')
        soup = BeautifulSoup(r.text,'html.parser')
        newsitems = soup.find_all('div',attrs={'class':'box'})
        curr_newsitem = newsitems[x]
        title=curr_newsitem.find('div',{'class':'box-text-title'}).text
        link=curr_newsitem.find('a')['href']
        date=curr_newsitem.find('div',{'class':'box-text-time'}).text
        d['title']=title
        d['link']=link
        d['date']=date
        articles.append((title,link,date))
        #l.append(d)
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
        d['title']=title
        d['link']=link
        d['date']=date
        z+=1
        w+=1
        if w%20==0:
            w-=20
            y+=1
            z+=1
        #l.append(d)
    return articles


if __name__ == "__main__":
    print(scrape())

extra_extra = pd.DataFrame(articles,columns=['Title','Link','Date'])
extra_extra.to_csv('yangste_news_' + now + '.csv',index=False,encoding='utf-8')
