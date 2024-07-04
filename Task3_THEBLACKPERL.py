import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

article_titles = []
for article in soup.find_all('article'):
    title = article.find('h2').text.strip()
    article_titles.append(title)

import csv
with open('article_titles.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title'])
    for title in article_titles:
        writer.writerow([title])

print("Data saved to article_titles.csv")
