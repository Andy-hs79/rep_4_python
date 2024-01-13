"""
Построить иерархию классов, удовлетворяющую следующим условиям (тематика иерархии на ваше усмотрение):
 - Количество классов >= 5.
 - Использовать наследование, в т.ч. множественное
 - Для каждого класса определить минимум 3 магических метода (на ваш выбор)
 - Создать экземпляры для каждого класса
 - Иерархия должна быть логичной и не противоречить принципам ООП.
"""
class Mammal:
    def __init__(self, kind):
        self.__kind = kind


class Animal(Mammal):
    def __init__(self, name, age, kind):
        super().__init__(kind)
        self.name = name
        self.__age = age

    def __str__(self):
        return f'kind - {self.__kind}, name - {self.name}, age - {self.__age} years'

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    age = property(fset=set_age, fget=get_age)


class Cat(Animal):
    def say(self):
        print("Mav")

class Dog(Animal):
    def say(self):
        print("Vaf")

class Human(Animal):
    def say(self):
        print("Hello world!")

dog1 = Dog("Bob", 5, "dog")
cat1 = Cat("Ulma", 3, "cat")
man1 = Human("Ivan", 33, "man")

dog1.say()
print(man1.age)

