# models.py
from functools import reduce

class Identifiable:
    def __init__(self, identifier):
        self.id = identifier

class Dish(Identifiable):
    def __init__(self, identifier, portion_size, price):
        super().__init__(identifier)
        self.portion_size = portion_size
        self.price = price

class CookedDish(Dish):
    def __init__(self, identifier, portion_size, price, preparation_time):
        super().__init__(identifier, portion_size, price)
        self.preparation_time = preparation_time

class Drink(Dish):
    def __init__(self, identifier, portion_size, price, alcohol_content):
        super().__init__(identifier, portion_size, price)
        self.alcohol_content = alcohol_content

class Customer(Identifiable):
    def __init__(self, identifier, name, address):
        super().__init__(identifier)
        self.name = name
        self.address = address

class Order(Identifiable):
    def __init__(self, identifier, customer_id, dish_ids, drink_ids, dish_repo, drink_repo):
        super().__init__(identifier)
        self.customer_id = customer_id
        self.dish_ids = dish_ids
        self.drink_ids = drink_ids
        self.total_cost = self.calculate_cost(dish_repo, drink_repo)

    def calculate_cost(self, dish_repo, drink_repo):
        # Fetch dish and drink objects based on IDs and sum their prices
        dish_prices = [dish_repo.get_by_id(dish_id).price for dish_id in self.dish_ids]
        drink_prices = [drink_repo.get_by_id(drink_id).price for drink_id in self.drink_ids]

        total_cost = sum(dish_prices) + sum(drink_prices)
        self.total_cost = total_cost
        return total_cost

    def generate_bill_string(self, dish_repo, drink_repo, customer_repo):
        # Fetch dish and drink objects based on IDs and customer object based on customer ID
        dishes = [dish_repo.get_by_id(dish_id) for dish_id in self.dish_ids]
        drinks = [drink_repo.get_by_id(drink_id) for drink_id in self.drink_ids]
        customer = customer_repo.get_by_id(self.customer_id)

        # Retrieve names and other attributes from the fetched objects
        dish_names = [f"{dish.id}: {dish.portion_size}g - ${dish.price:.2f}" for dish in dishes]
        drink_names = [f"{drink.id}: {drink.portion_size}ml - ${drink.price:.2f}" for drink in drinks]
        customer_name = customer.name

        bill_string = f"Bill for Customer {customer_name} (Order ID: {self.id}):\n"
        bill_string += "Dishes: " + ", ".join(dish_names) + "\n"
        bill_string += "Drinks: " + ", ".join(drink_names) + "\n"
        bill_string += f"Total Cost: ${self.total_cost:.2f}"

        return bill_string
