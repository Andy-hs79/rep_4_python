class Snow:
    """ Создать класс Snow. Класс содержит целое число - количество снежинок.  Класс включает методы перегрузки
    арифметических операторов сложения, вычитания, умножения и деления. Код этих методов должен выполнять увеличение
    или уменьшение количества снежинок на число n или в n раз. Класс также включает метод makeSnow(), который принимает
    сам объект и число снежинок в ряду, а возвращает строку вида "*****\\n*****\\n*****…", где количество снежинок
    между '\\n' равно переданному аргументу, а количество рядов вычисляется, исходя из общего количества снежинок."""

    def __init__(self, qty_snowflakes=5):
        self.qty_snowflakes = qty_snowflakes

    def __add__(self, other):
        match other:
            case Snow(): self.qty_snowflakes += other.qty_snowflakes
            case int(): self.qty_snowflakes += other

    def __sub__(self, other):
        match other:
            case Snow(): self.qty_snowflakes -= other.qty_snowflakes
            case int(): self.qty_snowflakes -= other

    def __mul__(self, other):
        match other:
            case Snow(): self.qty_snowflakes *= other.qty_snowflakes
            case int(): self.qty_snowflakes *= other

    def __truediv__(self, other):
        match other:
            case Snow(): self.qty_snowflakes //= other.qty_snowflakes
            case int(): self.qty_snowflakes //= other

    def makeSnow(self, snowflakes: int):  # тут, по идее, не "горбатый" стиль должен быть
        print(('*' * snowflakes + '\n') * (self.qty_snowflakes // snowflakes), end='')
        print('*' * (self.qty_snowflakes % snowflakes))

    def __str__(self):
        return str(self.qty_snowflakes)


snow1 = Snow(20)
snow2 = Snow(30)
print(snow2)
snow2 + 10
print(snow2)
snow2 + snow1
print(snow2)

snow2.makeSnow(13)


