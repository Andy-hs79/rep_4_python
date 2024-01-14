import requests
from bs4 import BeautifulSoup
import lxml


def download_page():
    url = "https://kormbosch.by/category/korm-dlja-sobak-bosch?page=1"
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
    }
    req = requests.get(url, headers=headers)
    src = req.text
    print(src)
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(src)


def main():
    with open("index.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    all_products = soup.find_all(class_="product")
    first_product = soup.find(class_="product")
    print(f'всего товаров - {len(all_products)}')
    for item in all_products:
        print(item.find('a').get('href'))
        print(item.find(class_="title").text.replace('\n', ''))
        print(f'price: {item.find(class_="price").text}')  # .replace('\n', '')}')


if __name__ == '__main__':
    #download_page()
    main()

