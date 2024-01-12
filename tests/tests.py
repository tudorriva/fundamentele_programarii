from repository.DrinkRepo import DrinkRepo
from repository.OrderRepo import OrderRepo
from modelle.Bestellung import Bestellung
from modelle.Getrank import Getrank
from repository.FoodRepo import FoodRepo
from modelle.GekochterGericht import GekochterGericht
from modelle.Kunde import Kunde
from repository.CustomerRepo import CustomerRepo
from ui.console import *
from controller.logic import deleteClient,updateClient,updateItem
from controller.logic import *


def test_searchClient_name():
    assert searchClient('Iva') != 0
    assert searchClient('yhyh') == 0

def test_searchClient_adress():
    assert searchClient('sel') != 0
    assert searchClient('ththt') == 0

def test_modifyClient():
    updateClient(3,'Victor','mircea Voda 16')
    assert getClient(3) == ('Victor', 'mircea Voda 16')


