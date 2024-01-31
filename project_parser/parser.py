import time
import requests
from bs4 import BeautifulSoup
import csv


def load_page(url, page: int = 1):
    # имитация работы с браузером
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
    for block in container:
    #for i in range(20, 23):
        #block = container[i]
        tmp += 1
        print(f'осталось {len(container) - tmp} ')
        url_block = block.find('a').get('href').replace('\n', '')
        if not url_block:
            url_block = 'no url_block'
            print('no url_block')
            continue

        weight_price.update(parse_products(url_block))
        time.sleep(2)

        title_block = block.find(class_="title").text.strip().replace('\n', '')
        if not title_block:
            title_block = 'no title_block'
            print('no title_block')
        for j in range(len(weight_price['price'])):
            if len(weight_price['price']) == 1:  # если товар в карточке один
                result.append({
                    'Название': title_block,
                    'Вес': 'Одиночный товар',
                    'Цена': weight_price['price'][0],
                    'Ссылка': url_block,
                })
            # если товары в карточке представлены вариативно
            else:
                result.append({
                    'Название': title_block,
                    'Вес': weight_price['weight'][j],
                    'Цена': weight_price['price'][j],
                    'Ссылка': url_block,
                })
    return result


def parse_products(url: str):
    text = load_page(url)
    soup = BeautifulSoup(text, "lxml")

    weights, prices = [], []
    result = {}
    if soup.find('div', class_="hcol-name_exp_last"):
        weights = soup.find_all('div', class_="hcol-name_exp_last")  # собираю веса товаров в карточке

    if len(weights) == 0:
        prices = [soup.find('div', class_="price")]
    else:
        prices = soup.find_all('span', class_=["hprice", 'hprice-new'])

    weights = [weight.text for weight in weights]  # получаю значения весов товаров из тэгов

    if len(prices):
        prices = [price.text for price in prices]  # получаю значения цен товаров из тэгов

        result.update({
            'price': prices,
            'weight': weights,
        })

    return result


def save_results(result):
    headers = ("Название", "Вес", "Цена", "Ссылка",)

    path = 'D:\\Andy\\rep_4_python\\project_parser\\data\\parsed_result.csv'
    with open(path, mode="w", encoding='utf-8') as file:
        file_writer = csv.DictWriter(file, delimiter=",", lineterminator="\r", fieldnames=headers)
        file_writer.writeheader()
        file_writer.writerows(result)



def run():
    result_page = []
    url_list = ['https://kormbosch.by/category/korm-dlja-sobak-bosch',
                'https://kormbosch.by/category/korm-dlja-kotov-sanabelle']
    for page in range(1, 3):
        text = load_page(url=url_list[0], page=page)
        result_page.extend(parse_page(text=text))
        time.sleep(2)
    text = load_page(url=url_list[1], page=1)
    result_page.extend(parse_page(text=text))
    print(result_page)

    print(f'всего результатов - {len(result_page)} ')
    save_results(result_page)


if __name__ == '__main__':
    run()
