from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import pandas as pd

def scalprum(*args, **options):

    # collecting from this link...
    html = urlopen('https://www.koton.com/tr/kadin/giyim/dis-giyim/kaban/c/M01-C02-N01-AK104-K100071')

    # converting to soup.
    soup = BeautifulSoup(html, 'html.parser')

    # grab all products inside the link...
    products = soup.find_all("div", class_="product-item")
    print(products)
    for p in products:
        pid = p.find('a', class_='prc-name')['href']
        title = p.find('a', class_='prc-name')
        images = {
            "img1": p.find('img', class_='swiper-slide-active')['src'],
            "img2": p.find('img', class_='swiper-slide-prev')['src'],
            "img3": p.find('img', class_='swiper-slide-duplicate-next')['src']
        }
        productCategory = p.find('h1').text
        colors = p.find('figcaption', class_='colors').text
        try:
            price = p.find('span', class_='firstPrice').text,
        except:
            price = p.find('span', class_='newPrice').text,
        currency = p.find('span', class_='newPrice' or 'firstPrice')[1].text,
        prices = {price, currency}
        badge = p.find('div', class_='product-badge').text,
        if badge == True:
            discount = True
        else:
            discount = False
        pcount = p.find('span', class_='plt-count').text # Total number of products 
        # checking for db
        try:
            # save in db
            Scraping.objects.create(
                pid=pid,
                title=title,
                images=images,
                productCategory=productCategory,
                colors=colors,
                prices=prices,
                discount=discount,
            )
            print('%s %s added' % (pid, title))
        except:
            print('%s %s already exists' % (pid, title))
    print(products)
    # self.stdout.write('scraping ended')
if __name__ == "__main__":
    scalprum()
    # df_bs = pd.DataFrame(products,columns=['pid','title','images', 'productCategory', 'colors', 'prices', 'discount'])
    # df_bs.set_index('pid',inplace=True)
    # print(df_bs.head(15))
    # df_bs.to_csv('output.csv')
    # print('s.txt', products)