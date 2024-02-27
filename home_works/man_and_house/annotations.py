from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Consumer:
    full_name: str
    account: str
    prefer: dict


@dataclass(frozen=True, slots=True)
class Shelter:
    price: str
    square: str
    house_type: str
    square_add: str
