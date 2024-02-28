class Consumer:
    def __init__(self, full_name, account, prefer):
        self.full_name = full_name
        self.account = account
        self.prefer = prefer

    def __str__(self):
        return str({"full_name": self.full_name, "account": self.account, "prefer": self.prefer})

    def __repr__(self):
        return (f"Name: {self.full_name}, money: {self.account}")

    def get_about(self):
        return {"Меня зовут: ": self.full_name, "Мой счет: ": self.account, "Мои предпочтения: ": self.prefer}


class Shelter:
    def __init__(self, price, square, house_type, square_add):
        self.price = price
        self.square = square
        self.house_type = house_type  # flat/house
        self.square_add = square_add

    def __str__(self):
        if self.square_add == 0 or self.square_add is None:
            return (f"Type: {self.house_type}, price: {self.price}, square: {self.square}")
        else:
            return (f"Type: {self.house_type}, price: {self.price}, square: {self.square}, add square: {self.square_add}")

    def __repr__(self):
        if self.square_add == 0 or self.square_add is None:
            return (f"Type: {self.house_type}, price: {self.price}, square: {self.square}")
        else:
            return (f"Type: {self.house_type}, price: {self.price}, square: {self.square}, add square: {self.square_add}")
