import requests
import pandas as pd
import os
from bs4 import BeautifulSoup


class HtmlParser:
    def __init__(self, url):
        self.url = url

    def get_title(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup.title.text

    def get_article(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, 'html.parser')
        for p in soup.find_all("p", {'class': True}):
            p.decompose()
        for a in soup.find_all("a"):
            a.decompose()
        temp_article = soup.find_all('p')
        article_1 = str(temp_article).replace("[", "").replace("]", "")
        return article_1

    # ============== Saving the file as text ==============
    def save_file(self, name, title, article):
        filename = f'{name}.txt'
        path = "./parsed_data"
        if not os.path.exists(path):
            os.makedirs(path)
        with open(os.path.join(path, filename), 'w', encoding="utf-8") as f:
            f.write(title)
            f.write("\n")
            soup = BeautifulSoup(article)
            f.write(soup.get_text())
    # ============== Saving the file as HTML ==============
    # def save_file(self,name,title,article):
    #     filename = f'{name}.html'
    #     path = "./parsed_data"
    #     if not os.path.exists(path):
    #         os.makedirs(path)
    #     with open(os.path.join(path, filename), 'w', encoding="utf-8") as f:
    #         f.write(f"<h1>{title}</h1>")
    #         f.write("\n")
    #         f.write(article)

# If the url is imported from xlsx,csv files
# data = pd.read_excel('./Input.xlsx')
# URL_ID = data['URL_ID'].tolist()
# URL = data['URL'].tolist()
for i in range(0, len(URL), 50):
    temp = HtmlParser(URL)
    title = temp.get_title()
    article = temp.get_article()
    temp.save_file(URL_ID, title, str(article))
