
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


def get_pagination(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = bs(response.text, 'html.parser')
            
            # Identify the pagination element and extract the number
            pagination_element = soup.find('div', class_='pagination')  # Adjust the class based on the actual HTML structure
            pagination_no = pagination_element.text.strip() if pagination_element else "No pagination found"
            
            return pagination_no
        else:
            return f"Failed to fetch page. Status code: {response.status_code}"

    except Exception as e:
        return f"An error occurred: {e}"

url = "https://press.et/?p=119795"
pagination_result = get_pagination(url)
print(f"There are: {pagination_result} pages on {url}")

