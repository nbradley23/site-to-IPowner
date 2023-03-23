import requests
from bs4 import BeautifulSoup

response = ''
response = requests.get('http://quotes.toscrape.com')
html = response.text
for page in range(2, 10):
    page_data = requests.get(
        'http://quotes.toscrape.com' + f'/page/{str(page)}/')
    html = html + page_data.text

soup = BeautifulSoup(html, 'html.parser')
qoute = soup.find_all('div', {'class': 'quote'})
print(qoute)
