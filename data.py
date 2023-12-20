import pandas as pd
from bs4 import BeautifulSoup
import requests
url = "https://midmart.com.bd/products"
res = requests.get(url)
htmlres = res.content

# print(htmlres)

soup = BeautifulSoup(htmlres , 'html.parser')

product_divs = soup.find_all('div', class_='axil-product product-style-one')

data = { 'Title': [], 'Href': [], 'Img': [], 'Current Price': [], 'Old Price': []}

for product_div in product_divs:

    anchor_tag = product_div.find('a')

    img_tag = anchor_tag.find('img')

    title_tag = product_div.find('h5', class_='title')

    current_price_tag = product_div.find('span', class_='price current-price')
    
    old_price_tag = product_div.find('span', class_='price old-price')
    
 
    data['Title'].append(title_tag.get_text(strip=True) if title_tag else None)
    data['Href'].append(anchor_tag.get('href') if anchor_tag else None)
    data['Img'].append(img_tag.get('src') if img_tag else None)
    data['Current Price'].append(current_price_tag.get_text(strip=True) if current_price_tag else None)
    data['Old Price'].append(old_price_tag.get_text(strip=True) if current_price_tag else None)

dataExcel = pd.DataFrame(data)
dataExcel.to_excel('output.xlsx', index=False)


  



