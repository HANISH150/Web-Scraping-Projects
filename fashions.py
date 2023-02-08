###code for trending fashions

import requests
import pandas as pd
from bs4 import BeautifulSoup
#declaring a list of trending items
list_of_trending_products=[]

#url of a website(fashion website)
url_of_website="https://thevou.com/fashion/current-fashion-trends/"
#getting request of the website
r=requests.get(url_of_website)
#using beautiful soup---> getting the required information
soup=BeautifulSoup(r.content,'html.parser')
#scraping trending products from the website information
items=soup.select('h2>strong>em')


for i in items:
    list_of_trending_products.append(i.text)

#displaying the trending products
for i in range(len(list_of_trending_products)):
    print(str(i+1)+"-->"+list_of_trending_products[i])

#selecting a trending product from list of displayed products
product_number=int(input("Enter a product number :"))
product_name=list_of_trending_products[product_number]

#declaring lists to store the title names,prices and image urls
list_of_titles=[]
list_of_prices=[]
list_of_imageURLs=[]

url_left = "https://www.flipkart.com/search?q="
url_right="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="

#url of selected product from flipkart website
url=url_left+product_name+url_right

#scraping the webpages and gathering the requrired information of the trending items
for pageNumbers in range(1,10):#loop for looping the pages of items in flipkart
    page_url =url + str(pageNumbers)
    r=requests.get(page_url)
    soup=BeautifulSoup(r.content,'html.parser')
    titles = soup.find_all('a',class_='IRpwTa')
    prices = soup.find_all('div',class_='_30jeq3')
    images= soup.select('img[src^="https://rukminim1.flixcart.com/image"]')
    for title,prices,image in zip(titles,prices,images):
        list_of_titles.append(title.text)
        list_of_prices.append(prices.text)
        list_of_imageURLs.append(image['src'])

data_in_dictionary_form={'titles':list_of_titles,'prices':list_of_prices,'image_urls':list_of_imageURLs}

data_frame=pd.DataFrame(data_in_dictionary_form)

print(data_frame)


