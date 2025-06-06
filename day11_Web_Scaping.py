import requests
from bs4 import BeautifulSoup
import json

base_url = 'http://quotes.toscrape.com'
next_page = '/page/1/'

all_quotes = []

while next_page:
    response = requests.get(base_url + next_page)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find('small', class_='author').get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]
        
        all_quotes.append({
            'text': text,
            'author': author,
            'tags': tags
        })

    next_btn = soup.find('li', class_='next')
    next_page = next_btn.find('a')['href'] if next_btn else None

# Save to JSON file
with open('all_quotes.json', 'w') as file:
    json.dump(all_quotes, file, indent=4)

print(f"Scraped {len(all_quotes)} quotes. Saved to 'all_quotes.json'.")
