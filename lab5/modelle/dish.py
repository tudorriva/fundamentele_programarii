# dish.py
from .identifiable import Identifiable

class Dish(Identifiable):
    def __init__(self, identifier, portion_size, price):
        super().__init__(identifier)
        self.portion_size = portion_size
        self.price = price
