import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests

def reviewExtractor(s):
    x = 0
    majorData = dict()
    r = requests.get('https://www.flipkart.com/search?q='+s)
    content = r.content
    wholeData = BeautifulSoup(content, "html.parser")
    subDataList = wholeData.findAll('a', attrs={'class':'_1fQZEK'})
    if len(subDataList) == 0:
        subDataList = wholeData.findAll('a', attrs={'class':'s1Q9rs'})
    for link in subDataList:
        x += 1
        print(x)
        if x>5:
            break
        try:
            productLink = link.attrs['href']
            r = requests.get('https://www.flipkart.com'+productLink)
            content = r.content
            soup = BeautifulSoup(content, "html.parser")
            print('B'*10)
            productName = soup.find('span', attrs={'class':'B_NuCI'}).text
            productPrice = soup.find('div', attrs={'class':'_30jeq3 _16Jk6d'}).text
            overAllRating = soup.find('div', attrs={'class':'_2d4LTz'}).text
            totalReviewsRatings = ' '.join([i.text for i in soup.findAll('div', attrs={'class':'row _2afbiS'})])
            ratings = {i+1:j.text for i,j in enumerate(soup.findAll('div', attrs={'class':'_1uJVNT'})[::-1])}
            reviewSection = soup.find('div', attrs={'class':'_2c2kV-'})
            reviewList = list()
            for i in soup.findAll('div', attrs={'class':'_2wzgFH'}):
                try:
                    rating = i.find('div', attrs={'class':'_3LWZlK _1BLPMq'}).text
                except:
                    rating = i.div.div.text
                title = i.find('p', attrs={'class':'_2-N8zT'}).text
                comment = i.find('div', attrs={'class':'t-ZTKy'}).text
                name = i.find('p', attrs={'class':'_2sc7ZR _2V5EHH'}).text
                upVotes, downVotes = [i.text for i in i.findAll('span', attrs={'class':'_3c3Px5'})]
                reviewList.append([rating, title, comment, name, upVotes, downVotes])

            majorData[productName]={\
                                   'Price':productPrice,
                                    'Over All Rating' : overAllRating,
                                    'Total Reviews & Ratings' : totalReviewsRatings,
                                    'starRatings' :ratings,
                                    'Review List' : reviewList
                                   }
        except:
            x -= 1

    return majorData
    #     break

def get_links_flipkart(s, n):
    base_url = r'https://www.flipkart.com'
    r = requests.get('https://www.flipkart.com/search?q='+s)
    content = r.content
    soup = BeautifulSoup(content,  "html.parser")

    link = soup.findAll('a', attrs={'class':'_1fQZEK'})
    links = list(map(lambda x: base_url + x.attrs['href'], link))
    for i in range(0, len(links), n):
        print(i, i+n)
        yield links[i:i+n]
    return len(list(map(lambda x: base_url + x.attrs['href'], link)))
links = get_links_flipkart('note9pro', 5)
# print(links)

for i in links:
    print(len(i))
# links
# print(__dir__())
# print(next(links))
