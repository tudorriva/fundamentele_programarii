# customer_repo.py
from .data_repo import DataRepo
from .repo_util import convert_to_string, convert_from_string, get_by_id
from modelle.customer import Customer

class CustomerRepo(DataRepo):
    def convert_to_string(self, customer_list):
        format_string = '{},{},{}'
        return convert_to_string(customer_list, format_string)

    def convert_from_string(self, content):
        split_char = ','
        return convert_from_string(content, split_char, Customer)

    def get_by_id(self, customer_id):
        customers = self.load()
        return get_by_id(customers, customer_id)

    def get_by_name(self, name):
        customers = self.load()
        for customer in customers:
            if customer.name.lower() == name.lower():
                return customer
        return None
