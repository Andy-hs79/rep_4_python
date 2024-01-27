import time
import requests
from bs4 import BeautifulSoup
import csv


def load_page(url, page: int = 1):
    session = requests.Session()
    session.headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
    }
    param = {
        'page': page
    }
    res = session.get(url, params=param)
    res.raise_for_status()
    return res.text


def parse_page(text: str):
    weight_price = {}
    result = []
    soup = BeautifulSoup(text, "lxml")
    container = soup.find_all(class_="product")
    print(f'всего товаров - {len(container)}')
    tmp = 0
    #for block in container:
    for i in range(5):
        block = container[i]
        tmp += 1
        print(tmp)
        url_block = block.find('a').get('href').replace('\n', '')
        if not url_block:
            url_block = 'no url_block'
            print('no url_block')
            continue

        weight_price.update(parse_products(url_block))
        time.sleep(2)

        title_block = block.find(class_="title").text.replace('\n', '')
        if not title_block:
            title_block = 'no title_block'
            print('no title_block')

        result.append({
            'Название': title_block,
            'Вес': weight_price['weight'],
            'Цена': weight_price['price'],
            'Ссылка': url_block,
        })
    return result


def parse_products(url: str):
    result = {}
    text = load_page(url)
    soup = BeautifulSoup(text, "lxml")
    weights, prices = [], []

    if soup.find('div', class_="hcol-name_exp_last"):
        weights = soup.find_all('div', class_="hcol-name_exp_last")  # собираю веса товаров в карточке
    if len(weights) == 0:
        prices = [soup.find('div', class_="price")]

    else:
        prices = soup.find_all('span', class_=["hprice", 'hprice-new'])

    weights = [weight.text for weight in weights]

    if len(prices):
        prices = [price.text for price in prices]

        result.update({
            'price': prices,
            'weight': weights,
        })

    return result


def save_results(result):
    HEADERS = ("Название", "Вес", "Цена", "Ссылка",)

    path = 'D:\\Andy\\rep_4_python\\project_parser\\data\\parsed_result_urls.csv'
    with open(path, mode="w", encoding='utf-8') as file:
        file_writer = csv.DictWriter(file, delimiter=",", lineterminator="\r", fieldnames=HEADERS)
        file_writer.writeheader()
        file_writer.writerows(result)



def run():
    result_page = []
    url_list = ['https://kormbosch.by/category/korm-dlja-sobak-bosch',
                'https://kormbosch.by/category/korm-dlja-kotov-sanabelle']
    # for page in range(1, 3):
    #     text = load_page(url=url_list[0], page=page)
    #     result_page.extend(parse_page(text=text))
    #     time.sleep(2)
    text = load_page(url=url_list[1], page=1)
    result_page.extend(parse_page(text=text))
    print(result_page)

    print(f'всего результатов - {len(result_page)} ')
    save_results(result_page)


if __name__ == '__main__':
    run()
