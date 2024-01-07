
from ui.ui import UI
from functools import reduce
from modelle.cooked_dish import CookedDish
from modelle.drink import Drink
from modelle.order import Order
from modelle.customer import Customer
from repository.cooked_dish_repo import CookedDishRepo
from repository.drink_repo import DrinkRepo
from repository.customer_repo import CustomerRepo
from repository.order_repo import OrderRepo

class Controller:
    def __init__(self, cooked_dish_repo, drink_repo, customer_repo, order_repo):
        self.cooked_dish_repo = cooked_dish_repo
        self.drink_repo = drink_repo
        self.customer_repo = customer_repo
        self.order_repo = order_repo

    def calculate_cost(self, customer_id, dishes, drinks):
        print(f"Calculating cost for order {self.order_repo.get_next_order_id()}")
        dish_costs = [self.cooked_dish_repo.get_by_id(dish_id).price for dish_id in dishes]
        drink_costs = [self.drink_repo.get_by_id(drink_id).price for drink_id in drinks]
        total_cost = sum(dish_costs) + sum(drink_costs)
        return total_cost

    def add_dish(self, dish):
        self.cooked_dish_repo.save([dish])

    def add_drink(self, drink):
        self.drink_repo.save([drink])

    def search_customer_by_partial_name(self, partial_name):
        customers = self.customer_repo.load()
        found_customers = [customer for customer in customers if partial_name.lower() in customer.name.lower()]
        return found_customers

    def search_customer_by_partial_address(self, partial_address):
        customers = self.customer_repo.load()
        found_customers = [customer for customer in customers if partial_address.lower() in customer.address.lower()]
        return found_customers

    def update_customer_name(self, customer_id, new_name):
        customers = self.customer_repo.load()
        for customer in customers:
            if customer.id == customer_id:
                customer.name = new_name
                self.customer_repo.save(customers)
                break

    def generate_bill_string(self, order_id):
        order = self.read_and_convert_order(order_id)
        if order:
            dish_names = [f"{dish.id}: {dish.portion_size}g - ${dish.price:.2f}" for dish_id in order.dish_ids for dish in self.cooked_dish_repo.load() if dish.id == dish_id]
            drink_names = [f"{drink.id}: {drink.portion_size}ml - ${drink.price:.2f}" for drink_id in order.drink_ids for drink in self.drink_repo.load() if drink.id == drink_id]

            bill_string = f"Order ID: {order.id}\nCustomer ID: {order.customer_id}\nDishes:\n{', '.join(dish_names)}\nDrinks:\n{', '.join(drink_names)}\nTotal Cost: ${order.total_cost:.2f}"

            # Remove the order after generating the bill
            self.order_repo.remove(order.id)
            return bill_string
        else:
            return "Order not found."

    def get_dishes(self):
        dishes = self.cooked_dish_repo.load()


        for dish in dishes:
            dish.price = float(dish.price)

        return dishes

    def get_drinks(self):
        drinks = self.drink_repo.load()


        for drink in drinks:
            drink.price = float(drink.price)

        return drinks

    def create_new_order(self, customer_name, dish_ids, drink_ids):
        customer = self.customer_repo.get_by_name(customer_name)
        if customer:
            dishes = [self.cooked_dish_repo.get_by_id(dish_id) for dish_id in dish_ids]
            drinks = [self.drink_repo.get_by_id(drink_id) for drink_id in drink_ids]

            if None in dishes or None in drinks:
                UI.display_message("One or more dishes or drinks not found.")
                return

            total_cost = self.calculate_cost(customer.id, dishes, drinks)
            new_order = Order(customer.id, dish_ids, drink_ids, total_cost, self.cooked_dish_repo, self.drink_repo)
            self.order_repo.add(new_order)
            UI.display_message(
                f"Order created successfully for customer {customer_name}. Total cost: ${total_cost:.2f}")
            return new_order
        else:
            UI.display_message("Customer not found.")
            return None

    def get_current_orders(self):
        return self.order_repo.load()

    def read_and_convert_order(self, order_id):
        orders = self.order_repo.load()
        for order in orders:
            if order.id == order_id:
                return order
        return None

    def add_new_customer(self, name, address):
        customers = self.customer_repo.load()
        new_customer_id = max([customer.id for customer in customers]) + 1 if customers else 1
        new_customer = Customer(new_customer_id, name, address)
        customers.append(new_customer)
        self.customer_repo.save(customers)
        return new_customer

    def get_customers(self):
        return self.customer_repo.load()
