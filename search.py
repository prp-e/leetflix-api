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
    #scraper = cloudscraper.create_scraper(browser={'browser' : 'chrome', 'platform' : 'windows'})
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0'})
    content = BeautifulSoup(response.content, 'lxml')
    links = content.findAll('a')
    for link in links:
        if 'magnet' in link['href']:
            return link['href']

def gather_data(keyword):
    urls = search_leet(keyword)
    data_gathered = []

    for url in urls:
        magnet = get_magnets(url['url'])
        url_data = {
            "url" : url['url'],
            "title": url['title'],
            "magnet": magnet
        }

        data_gathered.append(url_data)
    
    return data_gathered
