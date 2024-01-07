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



def display_menu():
    UI.display_message("1. Add Dish")
    UI.display_message("2. Add Drink")
    UI.display_message("3. Search for Customer by Partial Name")
    UI.display_message("4. Search for Customer by Partial Address")
    UI.display_message("5. Update Customer Name")
    UI.display_message("6. Generate Bill for an Order")
    UI.display_message("7. Display List of Dishes")
    UI.display_message("8. Display List of Drinks")
    UI.display_message("9. Create New Order")
    UI.display_message("10. Display Current Orders")
    UI.display_message("11. Add New Customer")
    UI.display_message("12. Display List of Customers")
    UI.display_message("13. Exit")

def main():
    cooked_dish_repo = CookedDishRepo('cooked_dishes.pkl')
    drink_repo = DrinkRepo('drinks.pkl')
    customer_repo = CustomerRepo('customers.pkl')
    order_repo = OrderRepo('orders.pkl')

    controller = Controller(cooked_dish_repo, drink_repo, customer_repo, order_repo)

    while True:
        display_menu()
        choice = UI.get_input("Enter your choice (1-13): ")

        if choice == "1":
            # Adding a Dish
            dish_id = UI.get_input("Enter dish ID: ")
            portion_size = UI.get_input("Enter portion size: ")
            price = UI.get_input("Enter price: ")
            preparation_time = UI.get_input("Enter preparation time: ")

            new_dish = CookedDish(dish_id, portion_size, price, preparation_time)
            controller.add_dish(new_dish)

        elif choice == "2":
            # Adding a Drink
            drink_id = UI.get_input("Enter drink ID: ")
            portion_size = UI.get_input("Enter portion size: ")
            price = UI.get_input("Enter price: ")
            alcohol_content = UI.get_input("Enter alcohol content: ")

            new_drink = Drink(drink_id, portion_size, price, alcohol_content)
            controller.add_drink(new_drink)

        elif choice == "3":
            # Search for a Customer by Partial Name
            partial_name = UI.get_input("Enter partial name: ")
            found_customers_by_name = controller.search_customer_by_partial_name(partial_name)
            UI.display_message(f"Customers with partial name '{partial_name}': {found_customers_by_name}")

        elif choice == "4":
            # Search for a Customer by Partial Address
            partial_address = UI.get_input("Enter partial address: ")
            found_customers_by_address = controller.search_customer_by_partial_address(partial_address)
            UI.display_message(f"Customers with partial address '{partial_address}': {found_customers_by_address}")

        elif choice == "5":
            # Updating a Customer Name
            customer_id_to_update = UI.get_input("Enter customer ID to update: ")
            new_customer_name = UI.get_input("Enter new customer name: ")
            controller.update_customer_name(customer_id_to_update, new_customer_name)

        elif choice == "6":
            # Generate Bill for an Order
            order_id_for_bill = UI.get_input("Enter order ID for bill generation: ")
            bill_string = controller.generate_bill_string(order_id_for_bill)
            UI.display_message(bill_string)

        elif choice == "7":
            # Display List of Dishes
            dishes = controller.get_dishes()
            UI.display_message("List of Dishes:")
            for dish in dishes:
                UI.display_message("{0}: {1}g - ${2:.2f}".format(dish.id, dish.portion_size, dish.price))

        elif choice == "8":
            drinks = controller.get_drinks()
            UI.display_message("List of Drinks:")
            for drink in drinks:
                UI.display_message("{0}: {1}ml - ${2:.2f}".format(drink.id, drink.portion_size, drink.price))

        elif choice == "9":
            customer_name = UI.get_input("Enter customer name for the new order: ")
            dish_ids = UI.get_input("Enter dish IDs (comma-separated): ").split(',')
            drink_ids = UI.get_input("Enter drink IDs (comma-separated): ").split(',')

            new_order = controller.create_new_order(customer_name, dish_ids, drink_ids)
            if new_order:
                UI.display_message(f"New order created with ID: {new_order.id}")
            else:
                UI.display_message("Failed to create a new order.")

        elif choice == "10":
            orders = controller.get_current_orders()
            UI.display_message("Current Orders:")
            for order in orders:
                UI.display_message(f"Order ID: {order.id}, Customer ID: {order.customer_id}, Total Cost: ${order.total_cost:.2f}")

        elif choice == "11":
            customer_name = UI.get_input("Enter customer name: ")
            customer_address = UI.get_input("Enter customer address: ")
            new_customer = controller.add_new_customer(customer_name, customer_address)
            if new_customer:
                UI.display_message(f"New customer added with ID: {new_customer.id}")
            else:
                UI.display_message("Failed to add a new customer.")

        elif choice == "12":
            customers = controller.get_customers()
            UI.display_message("List of Customers:")
            for customer in customers:
                UI.display_message(f"ID: {customer.id}, Name: {customer.name}, Address: {customer.address}")

        elif choice == "13":
            # Exit
            break

if __name__ == "__main__":
    main()
