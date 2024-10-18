from menuComponent import MenuComponent


class MenuItem(MenuComponent):
    name: str
    description: str
    price: float
    veg: bool

    def __init__(self, name: str, desc: str, price: int, veg: bool):
        self.name = name
        self.description = desc
        self.price = price
        self.veg = veg

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price

    def is_veg(self) -> bool:
        return self.veg

    def print(self):
        print(f"Name: {self.get_name()}")
        print(f"Description: {self.get_description()}")
        print(f"Price: {self.get_price()}")
        if self.is_veg():
            print("Vegetarian: Yes")
        else:
            print("Vegetarian: No")
        print('\n')