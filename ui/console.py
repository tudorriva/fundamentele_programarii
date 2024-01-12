from controller.logic import createMenu,searchClient,getOrders,getClients
from repository import FoodRepo, DrinkRepo, CustomerRepo



def showClientMenu():
    user_input = input("""
        1 -> show Menu
        2 -> order
        0 -> back to main menu
    """)

def requestID():
    id = input("id: ")
    return int(id)

def requestItemInfo():
    name=input("name: ")
    portionsgrosse = input("portionsgrosse: ")
    preis = input("preis: ")

    return name,portionsgrosse,preis

def food_or_drink():
    choice = input("""
        1 -> Drink
        2 -> Food
    """)

    return choice

def getClientInfo():
    name = input("name: ")
    adress = input("adress: ")

    return name, adress



def showResults(string):
    results = searchClient(string)
    if results != 0:
        for result in results:
            print(result)
        return 1
    else: return 0

def getOrderInfo():
    clientid = input("client id: ")

    drinksids = []
    while(True):
        id = int(input("drink id: "))
        if id > 0:
            drinksids.append(id)
        else:
            break

    foodids = []
    while(True):
        id = int(input("food id: "))
        if id > 0:
            foodids.append(id)
        else:
            break

    return clientid,drinksids,foodids



def showRestaurantMenu():
    menu = createMenu()
    for item in menu:
        print(item)

def client_or_item():
    choice = input("""
        1 -> Client
        2 -> Menu Item
        0 -> back
    """)

    return choice

def showClients():
    clients = getClients()
    for client in clients:
        print(client)

def showMainMenu():
    user_input = input("""
        -- Welcome to Restaurant Manager --
        Choose one of the following options:
        1 -> Add Item
        2 -> Delete Item
        3 -> Modify Item
        4 -> Search Client
        5 -> Create Bill
        6 -> Show Food Menu
        7 -> Show Drinks Menu
        8 -> Show Clients
        0 -> Exit
    """)
    return user_input


