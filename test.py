
from bs4 import BeautifulSoup
import requests
import  csv

URL = "https://www.keramogranit.ru/brands/alma-ceramica/"
HEADERS = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5045.139 Safari/537.36"
}
HOST = "https://www.keramogranit.ru"
FILE = 'plitka.csv'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('li', class_ = 'pager__item')
    if pagination:
        return int(pagination[-1].get_text()) 
    else:
        return 1

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'cat-card js-catcard')
    
    plitka = []      
           
    # for item in items:

    #     price = item.find('span', class_ = 'cat-card__price-cur')
    #     if price:
    #         price = price.get_text()
    #     else:
    #         price = 'Цену уточняйте!'

    #     id = item.find("meta")
    #     if id:
    #         id = id.get("content")
    #     else:
    #         id = "Проблема с Кодом"

    #     plitka.append({
    #         "title" : item.find('a', class_ ="cat-card__title-link").get_text(strip = True),
    #         "price" : price,
    #         "size" : item.find('dd').get_text(),
    #         "link" : HOST + item.find("a").get("href"),
    #         "id" : id,
    #         "image_link": HOST + item.find("img").get("src"),
    #         "style": item.find("dd").find_next("dd").get_text()      
    #     })      
    # return plitka  


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Код", "Брэнд/Название", "Размер", "Цена руб/кв.м", "Стиль", "Ссылка на товар", "Ссылка на фото"])
        for item in items:
            writer.writerow([item["id"], item["title"], item["size"], item["price"], item["style"], item["link"], item["image_link"]])
    
        
def parse():
    html = get_html(URL)
    if html.status_code == 200:
        plitka = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f"Идёт парсинг {page} из {pages_count}...")
            html = get_html(URL, params={'p': page })
            plitka.extend(get_content(html.text))
        save_file(plitka, FILE)
        print(f"Получено {len(plitka)} объектов")         
    else:
        print("Error")
parse()
    