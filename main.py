from tests.tests import *
from ui.console import *
import  pickle
from controller.logic import addClient,deleteItem,updateClient,updateItem,addItem,createBill
def main():
    #Tests ob alles richtig wirkt
    test_searchClient_adress()
    test_searchClient_name()
    test_modifyClient()

    while(True):
        choice = int(showMainMenu())
        if choice == 0:
            return
        elif choice == 1:
            item = int(client_or_item())
            if item == 1:
                name,adress = getClientInfo()
                addClient(name,adress)
            elif item == 2:
                type_of_item = int(food_or_drink())
                name,portionsgrosse,preis = requestItemInfo()
                addItem(name,portionsgrosse,preis,type_of_item)
        elif choice == 2:
            item = int(client_or_item())
            if item == 1:
                showClients()
                id = requestID()
                deleteClient(id)
            elif item == 2:
                showRestaurantMenu()
                id = requestID()
                deleteItem(id)
        elif choice == 3:
            item = int(client_or_item())
            if item == 1:
                showClients()
                id = requestID()
                name,adress = getClientInfo()
                updateClient(id,name,adress)
            elif item == 2:
                showRestaurantMenu()
                id = requestID()
                name,portionsgrosse,preis = requestItemInfo()
                updateItem(id,name,portionsgrosse,preis)
        elif choice == 4:
            keyword = input("search: ")
            showResults(keyword)
        elif choice == 5:
            keyword = input("search client: ")
            if showResults(keyword) == 0:
                name,adress = getClientInfo()
                addClient(name,adress)
                showClients()
            print('\n\n')
            showRestaurantMenu()
            clientID, drinksIDs, foodIDs = getOrderInfo()
            createBill(clientID, drinksIDs, foodIDs)
        elif choice == 6:
            showFood()
        elif choice == 7:
            showDrinks()
        elif choice == 8:
            showClients()

main()