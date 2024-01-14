import requests
from bs4 import BeautifulSoup
import collections
import csv


ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'name',
        'price',
        'url',
    ),
)
HEADERS = (
    'Название',
    "Цена",
    "Ссылка",
)


class Parser:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
        }
        self.result = []

    def load_page(self, page: int = 1):
        url = "https://kormbosch.by/category/korm-dlja-sobak-bosch"
        param = {
            'page': page
        }
        res = self.session.get(url, params=param)
        res.raise_for_status()
        return res.text

    def parse_page(self, text: str):
        soup = BeautifulSoup(text, "lxml")
        container = soup.find_all(class_="product")
        print(f'всего товаров - {len(container)}')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):
        url_block = block.find('a').get('href')
        if not url_block:
            print('no url_block')
            return
        title_block = block.find(class_="title").text.replace('\n', '')
        if not title_block:
            print('no title_block')
            return
        price_block = block.find(class_="price-new").text.replace('\n', '')
        if not price_block:
            price_block = block.find(class_="price").text.replace('\n', '')
            print(price_block)
        if not price_block:
            print('no price_block')
            return

        self.result.append(ParseResult(
            name=title_block,
            price=price_block,
            url=url_block,
        ))

    def save_results(self):
        # path = 'D:\\Andy\\rep_4_python\\project_parser\\data\\pars.csv'
        # with open(path, "w", encoding="utf-8") as file:
        #     writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        #     writer.writerow(HEADERS)
        #     for item in self.result:
        #         writer.writerow(item)
        print(self.result)
        path = 'D:\\Andy\\rep_4_python\\project_parser\\data\\parsed_result.csv'
        with open(path, "w", encoding="utf-8") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(HEADERS)
            writer.writerows(self.result)

    def run(self):
        for page in range(1, 3):
            text = self.load_page(page)
            self.parse_page(text=text)
            print(f'получили {len(self.result)} результатов')
        self.save_results()


if __name__ == '__main__':
    parser = Parser()
    parser.run()
