
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import requests

# Open a file in write mode
with open('scraped_data.txt', 'w', encoding='utf-8') as file:
    for i in range(1, 40):
        url = f'https://press.et/?paged={i}&cat=6'
        article = requests.get(url)
        soup = bs(article.content, "html.parser")
        links = soup.find(class_='entry-title').find_all('a')
        
        for link in links:
            link_text = link.get_text()
            link_href = link['href']
            file.write("Head Line: " + link_text + "\n")
            
            url1 = link_href
            nav_article = requests.get(url1)
            nav_soup = bs(nav_article.content, "html.parser")
            paragraphs = nav_soup.find(class_='entry-content').find_all('p')
            
            news_text = ""
            for p in paragraphs:
                news_text += str(p.get_text()) + "\n"
                file.write(p.get_text() + "\n")

            file.write("\n\n")  # Add some separation between articles
