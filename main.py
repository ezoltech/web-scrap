from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import requests
from datetime import datetime


def save_to_file(data, file_name):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(data + "\n")


def get_current_date():
    return datetime.now().strftime("%d%m%Y")


file_name = f"scraped_data_{get_current_date()}.txt"

for i in range(1, 40):
    url = f"https://press.et/?paged={i}&cat=6"
    article = requests.get(url)
    soup = bs(article.content, "html.parser")
    links = soup.find(class_="entry-title").find_all("a")

    for link in links:
        link_text = link.get_text()
        link_href = link["href"]
        data_to_save = f"Link Text: {link_text}, Href: {link_href}"
        save_to_file(data_to_save, file_name)

url1 = "https://press.et/?p=119795"
nav_article = requests.get(url1)
nav_soup = bs(nav_article.content, "html.parser")
links = nav_soup.find(class_="entry-content").find_all("p")
news_text = ""
for p in links:
    news_text = news_text + str(p.get_text())
    save_to_file(news_text, file_name)

for i in range(1, 10):
    url = "https://press.et/?paged=" + str(i) + "&amp;cat=149"
    nav_article = requests.get(url)
    nav_soup = bs(nav_article.content, "html.parser")
    links = nav_soup.find(id="secondary-bar").find_all("a")
    contents = nav_soup.find(id="recent-content").find_all("a")
    for link in contents:
        link_text = link.get_text()
        link_href = link["href"]
        data_to_save = f"Link Text: {link_text}, Href: {link_href}"
        save_to_file(data_to_save, file_name)


def get_pagination(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:

            soup = bs(response.text, "html.parser")

            pagination_element = soup.find("div", class_="pagination")
            pagination_no = (
                pagination_element.text.strip()
                if pagination_element
                else "No pagination found"
            )

            return pagination_no
        else:
            return f"Failed to fetch page. Status code: {response.status_code}"

    except Exception as e:
        return f"An error occurred: {e}"


url = "https://press.et/?p=119795"
pagination_result = get_pagination(url)
save_to_file(f"There are: {pagination_result} pages on {url}", file_name)


# def main_menu():
#     print("\t\twelcome please choose to continue\n\n\t\t\t\t")


