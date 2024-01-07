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
from controller.controller import Controller

def test_program_functionality():
    cooked_dish_repo = CookedDishRepo("cooked_dishes.pkl")
    drink_repo = DrinkRepo("drinks.pkl")
    customer_repo = CustomerRepo("customers.pkl")
    order_repo = OrderRepo("orders.pkl")

    controller = Controller(cooked_dish_repo, drink_repo, customer_repo, order_repo)

    customer_name = "John"
    dish_ids = [1, 2]
    drink_ids = [3, 4]
    new_order = controller.create_new_order(customer_name, dish_ids, drink_ids)

    assert isinstance(new_order, Order), "Error: Expected an Order object"

    viewed_order = controller.view_order(new_order.id)

    assert isinstance(viewed_order, Order), "Error: Expected an Order object"

    menu = controller.view_menu()

    assert isinstance(menu, list) and len(menu) > 0, "Error: Expected a non-empty list of menu items"

    customer_id = 1
    customer_orders = controller.view_customer_orders(customer_id)

    assert isinstance(customer_orders, list), "Error: Expected a list of customer orders"

if __name__ == "__main__":
    test_program_functionality()
