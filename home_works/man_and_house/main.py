from annotations import Consumer as a_Consumer, Shelter as a_Shelter
from fixtures import tuple_square_to_int, str_usd_to_int, str_square_to_int


def get_recs(house_list: list[a_Shelter], consumer: a_Consumer) -> list[a_Shelter]:
    print(consumer)
    if not house_list:
        return Exception("Нет домов")
    if not consumer:
        return Exception("Нет покупателя")

    prefered_house_type = consumer.prefer["house_type"]
    prefered_square = tuple_square_to_int(consumer.prefer["square"])
    prefered_price = str_usd_to_int(consumer.account)

    type_house_filter = filter(lambda x: x.house_type == prefered_house_type, house_list)
    price_house_filter = filter(lambda x: str_usd_to_int(x.price) <= prefered_price, type_house_filter)
    square_house_filter = filter(lambda x: str_square_to_int(x.square) in range(*prefered_square), price_house_filter)

    if prefered_house_type == "house":
        prefered_square_add = tuple_square_to_int(consumer.prefer["square_add"])
        square_add_house_filter = filter(lambda x: x.square_add in range(*prefered_square_add), square_house_filter)
        return list(square_add_house_filter)
    return list(square_house_filter)
