# cooked_dish.py
from .dish import Dish

class CookedDish(Dish):
    def __init__(self, identifier, portion_size, price, preparation_time):
        super().__init__(identifier, portion_size, price)
        self.preparation_time = preparation_time
