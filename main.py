page_data = {6: 10, 17: 10, 18: 10, 16: 10, 11: 10, 5: 10, 61: 10}
with open('AI_scraped_data.txt', 'w', encoding='utf-8') as file:
    for category, page_size in page_data.items():
            for i in range(1, page_size):
                url = f'https://press.et/?paged={i}&cat={category}'
                article = requests.get(url)
                soup = bs(article.content, "html.parser")
                links = soup.find(class_='entry-title').find_all('a')

                for link in links:
                    link_text = link.get_text()
                    link_href = link['href']
                    file.write("Head Line:"+ link_text)
                    #file.write("URL: " + link_href + "\n")

                    nav_article = requests.get(link_href)
                    nav_soup = bs(nav_article.content, "html.parser")
                    paragraphs = nav_soup.find(class_='entry-content').find_all('p')

                    for p in paragraphs:
                        file.write(p.get_text() + "\n")
                    file.write("\n\n")