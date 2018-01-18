import requests
import pandas as pd
from bs4 import BeautifulSoup

r = requests.get('http://www.yangtse.com/')
soup = BeautifulSoup(r.text,'html.parser')
'''
//*[@id="main"]/div[2]/div[7] - main
 //*[@id="main"]/div[2]/div[7]/div[1] - box white
   //*[@id="main"]/div[2]/div[7]/div[1]/div[2] - box text
    //*[@id="main"]/div[2]/div[7]/div[1]/div[2]/div[1] title
    //*[@id="main"]/div[2]/div[7]/div[1]/div[2]/div[2] time
    //*[@id="main"]/div[2]/div[7]/div[1]/div[2]/div[3] text
'''

#print(r.text[0:500])
#print(soup)

results = soup.find_all('div', attrs={'class':'box white'})
results2 = soup.find_all('div', attrs={'class':'box2 white'})
#print(len(results) + len(results2))

first_result = results[0]
#print(first_result)
first_link=first_result.find('a').text
first_date=first_result.find('span').text
first_text=first_result.find('div',{'class':'box-text-text'}).text

#print(first_link)
#print(first_date)
#print(first_text)

# second_result = results2[0]
#
# second_link=second_result.find('div',{'class': 'box2-name'}).text
#
# second_text=second_result.find('div',{'class':'box2-title'}).text
#
# print(second_link)
#
# print(second_text)

#main > div.main-right > div.main-right-main > div:nth-child(6) > div.box2-title > a
#main > div.main-right > div.main-right-main > div:nth-child(6) > div.box2-title > a



def news_stand(results,results2):
    top_one_hundred = []

    for x in range(0,len(results)):
        while len(top_one_hundred) <= 98: #final iteration adds 2
            section1=results[x]
            section2=results2[x]
            top_one_hundred.append('Title: ' + section1.find('a').text + ' , ' + 'Date: ' + section1.find('span').text + ' , ' + 'Article: ' + section1.find('div', {'class':'box-text-text'}).text)
            top_one_hundred.append('Title: ' + section2.find('div',{'class': 'box2-name'}).text + ' , ' + 'Date: ' + 'Unlisted Date , ' + 'Article: ' + section2.find('div',{'class':'box2-title'}).text )
            print(top_one_hundred)
            print(len(top_one_hundred))

news_stand(results,results2)
