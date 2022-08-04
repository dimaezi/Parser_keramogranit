
from bs4 import BeautifulSoup
import requests

headers = {
    'User-agent':'Mozilla/5.0 (Windows NT 11.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5102.127 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

URL = 'https://www.keramogranit.ru/brands/alma-ceramica/'
HOST = 'https://www.keramogranit.ru'

def get_html(url, params=None):
    r = requests.get(url, headers=headers, params=params)
    return r

def get_cards(html):
    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all('div', class_ = 'cat-card js-catcard')

    
    links = []

    for links in cards:  
        links.append({ 
            "link" : HOST + links.find('a').get('href')
        })
    return links




        
        


    

    


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        links = []
        get_cards(html.text)

        
    else:
        print('err')

parse()

