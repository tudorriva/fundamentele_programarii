from repository.FoodRepo import FoodRepo
from repository.DrinkRepo import DrinkRepo
from repository.OrderRepo import OrderRepo
from repository.CustomerRepo import CustomerRepo
from modelle.Kunde import Kunde
from modelle.Bestellung import Bestellung
from modelle.Getrank import Getrank
from modelle.GekochterGericht import GekochterGericht
import files


def getClients():
    client_repo = CustomerRepo('customers.pickle')
    clients = client_repo.load()
    return client_repo.convert_to_string(clients)

def getMenuObject():
    drink_repo = DrinkRepo('drinks.pickle')
    drinks = drink_repo.load()

    food_repo = FoodRepo('food.pickle')
    food = food_repo.load()

    return drinks + food

def addItem(name,portionsgrosse,preis,choice):
    menu = getMenuObject()
    menu_ids = [item.id for item in menu]
    if min(menu_ids) > 1:
        id = min(menu_ids) - 1
    else:
        id = max(menu_ids) + 1

    if choice == 1:
        drink_repo = DrinkRepo('drinks.pickle')
        drinks = drink_repo.load()
        alkoholgehalt = input("alkoholgehalt: ")
        drink = Getrank(id,name,portionsgrosse,preis,alkoholgehalt)
        drinks.append(drink)
        drink_repo.save(drinks)
    elif choice == 2:
        food_repo = FoodRepo('food.pickle')
        food = food_repo.load()
        zeit = input("zubereitungszeit: ")
        item = GekochterGericht(id,name,portionsgrosse,preis,zeit)
        food.append(item)
        food_repo.save(food)



def deleteClient(id):
    customer_repo = CustomerRepo('customers.pickle')
    customers = customer_repo.load()

    for customer in customers:
        if int(id) == customer.id:
            customers.remove(customer)
            break

    customer_repo.save(customers)


def updateClient(id,name,adress):
    customer_repo = CustomerRepo('customers.pickle')
    customers = customer_repo.load()

    for customer in customers:
        if int(id) == customer.id:
            customers.remove(customer)
            break

    newCustomer = Kunde(id,name,adress)
    customers.append(newCustomer)
    customer_repo.save(customers)

def deleteItem(id):
    drink_repo = DrinkRepo('drinks.pickle')
    food_repo = FoodRepo('food.pickle')
    drinks = drink_repo.load()
    food = food_repo.load()

    for drink in drinks:
        if int(id) == drink.id:
            drinks.remove(drink)
            break

    for item in food:
        if int(id) == item.id:
            food.remove(item)
            break

    drink_repo.save(drinks)
    food_repo.save(food)


def updateItem(id,name,portionsgrosse,preis):
    found = False
    drink_repo = DrinkRepo('drinks.pickle')
    food_repo = FoodRepo('food.pickle')
    drinks = drink_repo.load()
    food = food_repo.load()

    for drink in drinks:
        if int(id) == drink.id:
            drinks.remove(drink)
            found = True
            break
    if found == True:
        alkoholgehalt = input("alkoholgehalt: ")
        drink = Getrank(id,name,portionsgrosse,preis,alkoholgehalt)
        drinks.append(drink)
        drink_repo.save(drinks)
    else:
        for item in food:
            if int(id) == item.id:
                food.remove(item)
                break
        zeit = input("zubereitungszeit: ")
        item = GekochterGericht(id,name,portionsgrosse,preis,zeit)
        food.append(item)
        food_repo.save(food)


def getClient(id):
    name,adress = None,None
    client_repo = CustomerRepo('customers.pickle')
    clients = client_repo.load()
    for client in clients:
        if id == client.id:
            name = client.name
            adress = client.adresse

    return name,adress


def addClient(name,adress):
    customer_repo = CustomerRepo('customers.pickle')
    customers = customer_repo.load()

    customers_ids = [int(customer.id) for customer in customers]

    if min(customers_ids) > 1:
        id = min(customers_ids) - 1
    else:
        id = max(customers_ids) + 1

    client = Kunde(id,name,adress)
    customers.append(client)

    customer_repo.save(customers)


def createMenu():
    drink_repo = DrinkRepo('drinks.pickle')
    drinks = drink_repo.load()
    listOfDrinks = drink_repo.convert_to_string(drinks)

    food_repo = FoodRepo('food.pickle')
    food = food_repo.load()
    listOfFood = food_repo.convert_to_string(food)

    menu = listOfFood + listOfDrinks
    return menu


def searchClient(string):
    customer_repo = CustomerRepo('customers.pickle')
    customers = customer_repo.load()

    results = list(filter(lambda obj: string.lower() in obj.name.lower(), customers))

    if len(results) == 0:
        results = list(filter(lambda obj: string.lower() in obj.adresse.lower(), customers))

    if len(results) == 0:
        return 0

    return customer_repo.convert_to_string(results)


def createBill(kundenid,drinksids,foodids):
    drink_repo = DrinkRepo('drinks.pickle')
    food_repo = FoodRepo('food.pickle')

    order_repo = OrderRepo('orders.pickle')
    orders = order_repo.load()
    id = len(orders) + 1

    order = Bestellung(id,kundenid,foodids,drinksids)

    order.calculateCosts(drink_repo,food_repo)
    orders.append(order)
    order.showRechnung(drink_repo,food_repo)
    order_repo.save(orders)

def getOrders():
    order_repo = OrderRepo('orders.pickle')
    orders = order_repo.load()

    return order_repo.convert_to_string(orders)

def showFood():
    food_repo = FoodRepo('food.pickle')
    food = food_repo.load()
    for item in food:
        print(f"{item.name}:  ({item.portionsgrosse}g) - {item.preis}€")

def showDrinks():
    drink_repo = DrinkRepo('drinks.pickle')
    drinks = drink_repo.load()
    for item in drinks:
        print(f"{item.id}: {item.name} ({item.portionsgrosse}ml) - {item.preis}€ ({item.alkoholgehalt}% Alkohol)")


def showClients():
    customer_repo = CustomerRepo('customers.pickle')
    customers = customer_repo.load()
    for customer in customers:
        print(f"{customer.id}: {customer.name} - {customer.adresse}")
