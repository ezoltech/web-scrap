
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import requests

for i in range(1,10):
    url='https://press.et/?paged='+str(i)+'&amp;cat=149'
    nav_article = requests.get(url)
    nav_soup = bs(nav_article.content, "html.parser")
    links=nav_soup.find(id='secondary-bar').find_all('a')
    contents=nav_soup.find(id='recent-content').find_all('a')
    #print()
for link in contents:
    link_text = link.get_text()
    link_href = link['href']
    
    print(f"Link Text: {link_text}, Href: {link_href}")

def get_pagination():
    pagination_no = ""
    print("there are: " + pagination_no + "are there")