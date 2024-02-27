def str_usd_to_int(value: str):
    return int(value[1:])


def str_square_to_int(value: str):
    return int(value[:-2])


def tuple_square_to_int(value: (str, str)):
    return int(value[0][:-2]), int(value[1][:-2])

