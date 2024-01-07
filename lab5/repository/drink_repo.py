
from .data_repo import DataRepo
from .repo_util import convert_to_string, convert_from_string, get_by_id
from modelle.drink import Drink

class DrinkRepo(DataRepo):
    def convert_to_string(self, drink_list):
        format_string = '{},{},{},{}'
        return convert_to_string(drink_list, format_string)

    def convert_from_string(self, content):
        split_char = ','
        return convert_from_string(content, split_char, Drink)

    def get_by_id(self, drink_id):
        drinks = self.load()
        return get_by_id(drinks, drink_id)

    def load(self):
        loaded_data = super().load()
        print("Loaded Drinks:", loaded_data)
        return loaded_data
