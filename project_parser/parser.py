import requests
from bs4 import BeautifulSoup
import collections
import csv

ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'name',
        'weight',
        'price',
        'url',
    ),
)
HEADERS = ("Название", "Вес", "Цена", "Ссылка",)


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
    result = []
    soup = BeautifulSoup(text, "lxml")
    container = soup.find_all(class_="product")
    print(f'всего товаров - {len(container)}')

    for block in container:
        url_block = block.find('a').get('href').replace('\n', '')
        if not url_block:
            url_block = 'no url_block'
            print('no url_block')
            continue
        weight_price = parse_products(url_block)

        title_block = block.find(class_="title").text.replace('\n', '')
        if not title_block:
            title_block = 'no title_block'
            print('no title_block')

        result.append(ParseResult(
            name=title_block,
            weight=weight_price[0],
            price=weight_price[1],
            url=url_block,
        ))
    return result


def parse_products(url):
    src = load_page(url)
    soup = BeautifulSoup(src, "lxml")
    result, weights_container, price_container = [], [], []
    single_products = soup.find(class_="product_weights")  # если продукт один в карточке
    if single_products.text == '\n':
        return soup.find(class_="price").text
    else:
        weights_container = soup.find_all(class_="hcol-name_exp_last")  # собираю веса товаров в карточке
        if soup.find(class_="hprice-new"):
            price_container = soup.find_all(class_="hprice-new")  # если скидка есть беру класс hprice-new
        else:
            price_container = soup.find_all(class_="hprice")  # если нет, то класс hprice

    for block in weights_container:
        print(block.text)
    for block in price_container:
        print(block.text)

    result.append(weights_container)
    result.append(price_container)

    return result


def save_results(result):
    # path = 'D:\\Andy\\rep_4_python\\project_parser\\data\\pars.csv'
    # with open(path, "w", encoding="utf-8") as file:
    #     writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    #     writer.writerow(HEADERS)
    #     for item in self.result:
    #         writer.writerow(item)
    # print(self.result)
    path = 'D:\\Andy\\rep_4_python\\project_parser\\data\\parsed_result_urls.csv'
    with open(path, "w", encoding="utf-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(HEADERS)
        writer.writerows(result)


def run():
    result_page = []
    url_list = ['https://kormbosch.by/category/korm-dlja-sobak-bosch',
                'https://kormbosch.by/category/korm-dlja-kotov-sanabelle']
    for page in range(1, 3):
        text = load_page(url=url_list[0], page=page)
        result_page.extend(parse_page(text=text))
    text = load_page(url=url_list[1], page=1)
    result_page.extend(parse_page(text=text))

    print(f'получили {len(result_page)} результатов')
    save_results(result_page)


if __name__ == '__main__':
    run()
