#THESE PRODUCTS ARE NOT FASHION ITEMS BUT THEY ARE TRENDING

from numpy import true_divide
import requests
import pandas as pd
from bs4 import BeautifulSoup

#getting product name
product_name=input("Enter a product name :")

url_left = "https://www.flipkart.com/search?q="
url_right="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="
url=url_left+product_name+url_right
#lists to store information
list_of_titles=[]
list_of_prices=[]
list_of_ratings=[]
list_of_reviews=[]
list_of_imageURLs=[]


################################################################################################################################
for pageNumbers in range(1,10):
    page_url = url + str(pageNumbers)
    r=requests.get(page_url)
    soup=BeautifulSoup(r.content,'html.parser')
    #print(soup)
    titles = soup.find_all('div',class_='_4rR01T')
    prices = soup.find_all('div',class_='_30jeq3 _1_WHN1')
    ratings = soup.find_all('span',class_='_1lRcqv')
    images = soup.select('img[src^="https://rukminim1.flixcart.com/image/312/312"]')
    for title,prices,rating,image in zip(titles,prices,ratings,images):
        list_of_titles.append(title.text)
        list_of_prices.append(prices.text)
        list_of_ratings.append(float(rating.text))
        list_of_reviews.append(rating.next_sibling.text)
        list_of_imageURLs.append(image['src'])

################################################################################################################################
if(len(list_of_titles)==0 and len(list_of_prices)==0 and len(list_of_reviews)==0 and len(list_of_ratings)==0):
    page_url = url + str(pageNumbers)
    r=requests.get(page_url)
    soup=BeautifulSoup(r.content,'html.parser')
    #print(soup)
    titles = soup.find_all('a',class_='s1Q9rs')
    prices = soup.find_all('div',class_='_30jeq3')
    ratings = soup.find_all('div',class_='_3LWZlK')
    ratings_number = soup.find_all('span',class_='_2_R_DZ')
    images=soup.select('img[src^="https://rukminim1.flixcart.com/image/612/612"]')
    for title,prices,rating,rating_number,image in zip(titles,prices,ratings,ratings_number,images):
        list_of_titles.append(title.text)
        list_of_prices.append(prices.text)
        list_of_ratings.append(float(rating.text))
        list_of_reviews.append(rating_number.text)
        list_of_imageURLs.append(image['src'])


for i in range(len(list_of_reviews)):
    str=list_of_reviews[i]
    temp=str.split()
    store=''
    for s in temp[0]:
        if(s>='0' or s<='9' and s!=',' and s!='(' and s!=')'):
            store=store+(s)
    list_of_reviews[i]=int(store)


###############################################################################################################################
for i in range(len(list_of_ratings)):
    list_of_ratings[i]=float(list_of_ratings[i])

#sorting products based on ratings and no.of ratings
for n in range(len(list_of_ratings)-1, 0, -1):
        for i in range(n):
            if list_of_ratings[i] == list_of_ratings[i + 1]:
                if list_of_reviews[i]<list_of_reviews[i+1]:
                    list_of_ratings[i], list_of_ratings[i + 1] = list_of_ratings[i + 1], list_of_ratings[i]
                    list_of_prices[i],list_of_prices[i+1]=list_of_prices[i+1],list_of_prices[i]
                    list_of_titles[i],list_of_titles[i+1]=list_of_titles[i+1],list_of_titles[i]
                    list_of_reviews[i],list_of_reviews[i+1]=list_of_reviews[i+1],list_of_reviews[i]
                    list_of_imageURLs[i],list_of_imageURLs[i+1]=list_of_imageURLs[i+1],list_of_imageURLs[i]
            elif list_of_ratings[i] < list_of_ratings[i + 1]:
                list_of_ratings[i], list_of_ratings[i + 1] = list_of_ratings[i + 1], list_of_ratings[i]
                list_of_prices[i],list_of_prices[i+1]=list_of_prices[i+1],list_of_prices[i]
                list_of_titles[i],list_of_titles[i+1]=list_of_titles[i+1],list_of_titles[i]
                list_of_reviews[i],list_of_reviews[i+1]=list_of_reviews[i+1],list_of_reviews[i]
                list_of_imageURLs[i],list_of_imageURLs[i+1]=list_of_imageURLs[i+1],list_of_imageURLs[i]


data_dictionary={'titles':list_of_titles,'prices':list_of_prices,'ratings':list_of_ratings,'no.of reviews':list_of_reviews,'image_urls':list_of_imageURLs}

data_frame=pd.DataFrame(data_dictionary)
print(data_frame)