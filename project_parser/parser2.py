import requests
from bs4 import BeautifulSoup
import collections
import csv
import time

ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'name',
        'price',
        'url',
    ),
)
HEADERS = ('Название', "Цена", "Ссылка",)


def load_page(url, page: int = 1):
    session = requests.Session()
    session.headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
    }
    res = session.get(url)
    res.raise_for_status()
    return res.text


def parse_products(text: str):
    result = []
    soup = BeautifulSoup(text, "lxml")
    weights_container, price_container = [], []
    single_products = soup.find(class_="product_weights")  # если продукт один в карточке
    if single_products.text == '\n':
        price = soup.find(class_="price").text
    else:
        weights_container = soup.find_all(class_="hcol-name_exp_last")  # собираю веса товаров в карточке
        if soup.find(class_="hprice-new"):
            price_container = soup.find_all(class_="hprice-new")  # если скидка есть беру класс hprice-new
        else:
            price_container = soup.find_all(class_="hprice")  # если нет, то класс hprice

    print(price)
    for block in weights_container:
        print(block.text)
    for block in price_container:
        print(block.text)

        # result.append(ParseResult(
        #     name=title_block,
        #     price=price_block,
        #     url=url_block,
        # ))

        # print(f'всего товаров - {len(container)}')
    return result


def save_results(result):
    path = 'D:\\Andy\\rep_4_python\\project_parser\\data\\parsed_result.csv'
    with open(path, "w", encoding="utf-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(HEADERS)
        writer.writerows(result)


def run():
    result_page = []
    url_list = ['https://kormbosch.by/product/korm-dlja-koshek-ot-goda-s-chuvstvitelnoj-polovoj-sistemoj-sanabelle-urinari-sanabell-jurineri-0-4kg',
                'https://kormbosch.by/product/bosch-breeder-lamb-and-rice-bosh-brider-jagnenok-s-risom20kg',
                'https://kormbosch.by/product/bosch-mini-adult-with-lamb-and-rice-bosh-mini-edalt-jagnenok-s-risom-korm-dlja-vzroslyx-sobak-melkix-porod-3kg']
    for i in range(3):
        text = load_page(url=url_list[i])
        result_page.extend(parse_products(text=text))
        time.sleep(2)

    print(f'получили {len(result_page)} результатов')
    #save_results(result_page)


if __name__ == '__main__':
    run()
