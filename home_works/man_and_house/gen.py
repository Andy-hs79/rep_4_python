from random import randint, choice
from typing import List

from annotations import Consumer as a_Consumer, Shelter as a_Shelter
from models import Consumer, Shelter
from const import NAMES, SURNAMES


def gen_consumer_object() -> a_Consumer:
    full_name = f"{choice(NAMES)} {choice(SURNAMES)}"
    account = "$" + str(randint(70_000, 200_000))
    prefer = {"house_type": choice(["house", "flat"]),
              "square": (str(randint(10, 40)) + "m2",
                         str(randint(50, 200)) + "m2")}
    if prefer["house_type"] == "house":
        prefer["square_add"] = (str(randint(50, 80)) + "m2",
                                str(randint(90, 300)) + "m2")
    consumer = Consumer(full_name=full_name, account=account, prefer=prefer)
    return consumer


def gen_house_objects(count: int) -> List[a_Shelter]:
    house_list = []
    for _ in range(count):
        price = "$" + str(randint(70_000, 200_000))
        square = str(randint(10, 200)) + "m2"
        house_type = choice(["house", "flat"])
        if house_type == "house":
            square_add = str(randint(50, 300)) + "m2"
        else:
            square_add = 0
        house = Shelter(price=price, square=square, house_type=house_type, square_add=square_add)
        house_list.append(house)
    return house_list
