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
    # Initialize repositories
    cooked_dish_repo = CookedDishRepo("cooked_dishes.pkl")
    drink_repo = DrinkRepo("drinks.pkl")
    customer_repo = CustomerRepo("customers.pkl")
    order_repo = OrderRepo("orders.pkl")

    # Initialize controller
    controller = Controller(cooked_dish_repo, drink_repo, customer_repo, order_repo)

    # Test creating a new order
    customer_name = "John"
    dish_ids = [1, 2]
    drink_ids = [3, 4]
    new_order = controller.create_new_order(customer_name, dish_ids, drink_ids)

    # Check if the new order is an instance of the Order class
    assert isinstance(new_order, Order), "Error: Expected an Order object"

    # Test viewing the order
    viewed_order = controller.view_order(new_order.id)

    # Check if the viewed order is an instance of the Order class
    assert isinstance(viewed_order, Order), "Error: Expected an Order object"

    # Test viewing the menu
    menu = controller.view_menu()

    # Check if the menu is a non-empty list
    assert isinstance(menu, list) and len(menu) > 0, "Error: Expected a non-empty list of menu items"

    # Test viewing customer orders
    customer_id = 1
    customer_orders = controller.view_customer_orders(customer_id)

    # Check if the customer orders is a list
    assert isinstance(customer_orders, list), "Error: Expected a list of customer orders"

if __name__ == "__main__":
    test_program_functionality()
