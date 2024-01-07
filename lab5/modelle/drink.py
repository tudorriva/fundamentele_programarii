
from .dish import Dish

class Drink(Dish):
    def __init__(self, identifier, portion_size, price, alcohol_content):
        super().__init__(identifier, portion_size, price)
        self.alcohol_content = alcohol_content
