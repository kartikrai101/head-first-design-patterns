# class for creating instances of menu items
class MenuItem:
    name: str
    description: str
    price: float
    is_veg: bool

    def __init__(self, name: str, desc: str, price: float, is_veg: bool):
        self.name = name
        self.description = desc
        self.price = price
        self.is_veg = is_veg

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price

    def is_veg(self) -> bool:
        return self.is_veg