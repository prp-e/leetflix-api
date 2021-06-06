from bs4 import BeautifulSoup
import cloudscraper
import lxml.html 
import requests


def search_leet(keyword):
    url = f"https://www.1377x.to/sort-search/{keyword}/seeders/desc/1/"
    response = requests.get(url)
    content = BeautifulSoup(response.text, 'lxml')

    data = []

    table_cells = content.findAll('td', {"class" : "name"})
    for cell in table_cells[5:]:
        cell = cell.findAll('a')
        cell = cell[1]
        data_dic = {"title" : cell.text, "url" : cell['href']}
        data.append(data_dic)

    return data

def get_magnets(url):
    url = "https://1337x.to" + url 
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)
    content = BeautifulSoup(response.content, 'lxml')
    links = content.findAll('a')
    for link in links:
        if 'magnet' in link['href']:
            return link['href']

if __name__ == "__main__":
    results = search_leet("v for vendetta")
    magnets = get_magnets(results[0]['url'])

    print(magnets)
    
