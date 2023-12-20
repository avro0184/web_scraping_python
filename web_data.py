import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_multiple_pages(total_page):
    data = {'Title': [], 'Href': [], 'Img': [], 'Current Price': [], 'Old Price': []}
    for page_num in range(total_page):
        url = f"https://midmart.com.bd/products?page={page_num}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')        
        product_divs = soup.find_all('div', class_='axil-product product-style-one')       
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
            data['Old Price'].append(old_price_tag.get_text(strip=True) if old_price_tag else None)           
    return data

print("How many page data do you want to print : ")
total_page = int(input())
print("Write output file name : ")
output_name = input()
scraped_data = scrape_multiple_pages(total_page)
# print(scraped_data)
dataExcel = pd.DataFrame(scraped_data)
dataExcel.to_excel(f'{output_name}.xlsx', index=False)

