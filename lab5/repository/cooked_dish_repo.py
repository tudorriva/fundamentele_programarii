
from .data_repo import DataRepo
from .repo_util import convert_to_string, convert_from_string, get_by_id
from modelle.cooked_dish import CookedDish

class CookedDishRepo(DataRepo):
    def convert_to_string(self, dish_list):
        format_string = '{},{},{},{}'
        return convert_to_string(dish_list, format_string)

    def convert_from_string(self, content):
        split_char = ','
        return convert_from_string(content, split_char, CookedDish)

    def get_by_id(self, dish_id):
        dishes = self.load()
        return get_by_id(dishes, dish_id)

    def load(self):
        loaded_data = super().load()
        print("Loaded Cooked Dishes:", loaded_data)
        return loaded_data
