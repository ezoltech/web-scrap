from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import requests

for i in range(1, 40):
    url = f'https://press.et/?paged={i}&cat=6'
    article = requests.get(url)
    soup = bs(article.content, "html.parser")
    links=soup.find(class_='entry-title').find_all('a')
    #print(links)
    for link in links:
        link_text = link.get_text()
        link_href = link['href']
        print(f"Link Text: {link_text}, Href: {link_href}")
        
url1='https://press.et/?p=119795'
nav_article = requests.get(url1)
nav_soup = bs(nav_article.content, "html.parser")
links=nav_soup.find(class_='entry-content').find_all('p')
news_text=""
for p in links:
    news_text=news_text+str(p.get_text())
    #print(p.get_text())

