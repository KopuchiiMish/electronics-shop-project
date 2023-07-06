from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self) -> str:
        return self.name

    def __add__(self, other):
        if issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        return None
        # if not isinstance(other, Item):
        #     raise ValueError('.')
        # return self.quantity + other.quantity


phone1 = Phone("iPhone 14", 120_000, 5, 2)
item1 = Item("Смартфон", 10000, 20)

result = phone1 + item1
print(result)
