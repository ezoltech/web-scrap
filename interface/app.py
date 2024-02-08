from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime

app = Flask(__name__)


def scrape_website(url):
    try:
        article = requests.get(url)
        soup = bs(article.content, "html.parser")
        paragraphs = soup.find(class_="entry-content").find_all("p")
        scraped_data = ""
        for p in paragraphs:
            scraped_data += p.get_text() + "\n"
        return scraped_data
    except Exception as e:
        return f"Error scraping website: {e}"


def save_to_file(data, file_name):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(data + "\n")


def get_current_date():
    return datetime.now().strftime("%d%m%Y")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/scrape", methods=["POST"])
def scrape():
    page_data = {6: 10, 17: 10, 18: 10, 16: 10, 11: 10, 5: 10, 61: 10}
    file_name = f"scraped_data_{get_current_date()}.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        for category, page_size in page_data.items():
            for i in range(1, page_size):
                url = f"https://press.et/?paged={i}&cat={category}"
                article = requests.get(url)
                soup = bs(article.content, "html.parser")
                links = soup.find(class_="entry-title").find_all("a")

                for link in links:
                    link_text = link.get_text()
                    link_href = link["href"]
                    file.write("Head Line:" + link_text)
                    nav_article = requests.get(link_href)
                    nav_soup = bs(nav_article.content, "html.parser")
                    paragraphs = nav_soup.find(class_="entry-content").find_all("p")
                    for p in paragraphs:
                        file.write(p.get_text() + "\n")
                    file.write("\n\n")
    with open(file_name, "r", encoding="utf-8") as file:
        scraped_data = file.read()
    return render_template("index.html", scraped_data=scraped_data)


if __name__ == "__main__":
    app.run(debug=True)
