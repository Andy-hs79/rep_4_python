from bs4 import BeautifulSoup
html_doc = """
<div class="example">
<p>bla-bla-bla</p>
<div>something not important</div>
<strong>SomeText</strong>
<br>
Нужный текст
<span style="color:red">Тоже нужный текст</span>
Нужный текст
</div>
"""
soup = BeautifulSoup(html_doc, "lxml")
tag = soup.find("div", class_="example")

tag.div.decompose() # убираем вложенный div
tag.p.decompose()  # убираем текст в теге <p>
tag.br.decompose() # убираем перенос <br>
print(tag)