"""Есть class Human, характеристиками которого являются:
Имя
Возраст
Наличие денег
Наличие собственного жилья
Человек может:
Предоставить информацию о себе
Заработать деньги
Купить дом

Также же есть class Дом, к свойствам которого относятся:
Площадь
Стоимость
Для Дома можно:
Применить скидку на покупку

Задание:
Реализовать описанную структуру и проверить методы предоставления скидки и приобретения дома. Сгенерировать несколько
экземпляров класса Дом и Human. Далее написать функцию, которая подберет наилучший дом для человека, на основании
площади и кол-ва денег у него на счету, а так же выведет список домов, которые можно рекомендовать. Параметры для
рекомендации можно выбрать любые. Например, если применить скидку стоимость дома будет подходящей, если человек
заработает еще, стоимость так же будет подходящей."""
# 2. Функции генерации объектов:
# gen_house_objects(count: int) -> List[object(Shelter)]
# gen_consumer_object() -> object(Consumer)
# 3. Функция подбора:
# get_recommendations(List[object(Shelter)], object(Consumer))
# 4. Функции работы с excel. in and out

class Human:
    def __init__(self, name: str, age: int, money: int, have_home: bool):
        self.name = name
        self.age = age
        self.money = money
        self.have_home = have_home

    def earn_money(self, amound):
        self.money += amound

    def introduce_self(self):
        return f'Меня зовут {self.name},\nу меня есть счет в размере {self.money} руб.'


class House:
    def __init__(self, square, cost):
        self.square = square
        self.cost = cost


if __name__ == '__main__':
    man1 = Human('John', 32, 50_000, False)
    print(man1.introduce_self())
    man1.earn_money(20_000)
    print(man1.introduce_self())
