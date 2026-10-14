import pandas as pd
from bs4 import BeautifulSoup
import requests
import threading

result = {}

def get_all_book(n):
    books_data = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    for i in range(1, n + 1):
        url = f"https://books.toscrape.com/catalogue/page-{i}.html"
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        bs = BeautifulSoup(response.content, 'html.parser')

        for p in bs.find_all('article', class_='product_pod'):
            title_tag = p.find('h3').find('a')
            price_tag = p.find('p', class_='price_color')
            stock_tag = p.find('p', class_='availability')
            rating_tag = p.find('p', class_='star-rating')

            books_data.append({
                'link': title_tag['href'],
                'book': title_tag['title'],
                'rate': price_tag.get_text(strip=True),
                'stock': stock_tag.get_text(strip=True),
                'rating': rating_tag.get('class')[1] if rating_tag else None
            })

    return pd.DataFrame(books_data)


def create_df(n):
    result['df'] = get_all_book(n)


thread = threading.Thread(target=create_df, args=(50,))
thread.start()
thread.join()  # Wait until scraping finishes

df = result['df']
print("Total books scraped:", len(df))
df.to_csv("books.csv", index=False)
