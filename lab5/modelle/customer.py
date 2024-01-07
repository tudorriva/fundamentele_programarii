# customer.py
from .identifiable import Identifiable

class Customer(Identifiable):
    def __init__(self, identifier, name, address):
        super().__init__(identifier)
        self.name = name
        self.address = address
