
from .data_repo import DataRepo
from .repo_util import convert_to_string, convert_from_string, get_by_id
from modelle.order import Order

class OrderRepo(DataRepo):
    def convert_to_string(self, order_list):
        format_string = '{},{},{},{},{}'
        return convert_to_string(order_list, format_string)

    def convert_from_string(self, content):
        split_char = ','
        return convert_from_string(content, split_char, Order)

    def get_by_id(self, order_id):
        orders = self.load()
        return get_by_id(orders, order_id)
