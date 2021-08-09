import requests
from bs4 import BeautifulSoup

URL = "https://www.avito.ru/moskva/noutbuki/apple-ASgBAgICAUSEK_a2Ag?cd=1"
HOST = "www.avito.ru"

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36)', 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='iva-item-content-m2FiN')
    objects = []
    for item in items:
        title = item.find('h3', class_='title-root-395AQ iva-item-title-1Rmmj title-listRedesign-3RaU2 title-root_maxHeight-3obWc text-text-1PdBw text-size-s-1PUdo text-bold-3R9dt')
        link = item.find('a').get('href')
        price = item.find('span', class_='price-text-1HrJ_ text-text-1PdBw text-size-s-1PUdo')
        location = item.find('div', class_='geo-georeferences-3or5Q text-text-1PdBw text-size-s-1PUdo')
        time = item.find('div', class_='date-text-2jSvU text-text-1PdBw text-size-s-1PUdo text-color-noaccent-bzEdI')

        if price:
            price = price.text.replace('\xa0', '').strip('₽')
        else:
            price = '0'
        if title != None:
            objects.append({
                'title': title.text,
                'link': HOST + link,
                 'price': price,
                 'location': location.text.rsplit()[0].replace(',', ''),
                 'time': time.text,
                })
    return(objects)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        objects = get_content(html.text)
    else:
        print('Error')
    return objects



def result():
    items = parse()
    data = []
    for item in items:
        str = (item['title'] + "\n" + item['price'] + "\n" + item['link'] + "\n" + item['location'] + "\n" + item['time']+ "\n")
        data.append(str)
    return ("".join(data))

print(result())