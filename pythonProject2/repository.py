# repository.py
import pickle

class DataRepo:
    def __init__(self, file_name):
        self.file = file_name

    def save(self, data):
        with open(self.file, 'wb') as f:
            pickle.dump(data, f)

    def load(self):
        with open(self.file, 'rb') as f:
            return pickle.load(f)

    def read_file(self):
        with open(self.file, 'r') as f:
            return f.read()

    def write_to_file(self, content):
        with open(self.file, 'w') as f:
            f.write(content)

    def convert_to_string(self, obj_list):
        # This method should be defined in subclasses
        pass

    def convert_from_string(self, content):
        # This method should be defined in subclasses
        pass

    def get_by_id(self, obj_id):
        for obj in self.load():
            if hasattr(obj, 'id') and obj.id == obj_id:
                return obj
        return None

class CookedDishRepo(DataRepo):
    def convert_to_string(self, dish_list):
        return '\n'.join([f'{dish.id},{dish.portion_size},{dish.price},{dish.preparation_time}' for dish in dish_list])

    def convert_from_string(self, content):
        dish_data = [line.split(',') for line in content.split('\n')]
        return [CookedDish(int(data[0]), int(data[1]), float(data[2]), int(data[3])) for data in dish_data if data]

    def get_by_id(self, dish_id):
        dishes = self.load()
        for dish in dishes:
            if dish.id == dish_id:
                return dish
        return None

    def load(self):
        loaded_data = super().load()
        print("Loaded Cooked Dishes:", loaded_data)
        return loaded_data

class DrinkRepo(DataRepo):
    def convert_to_string(self, drink_list):
        return '\n'.join([f'{drink.id},{drink.portion_size},{drink.price},{drink.alcohol_content}' for drink in drink_list])

    def convert_from_string(self, content):
        drink_data = [line.split(',') for line in content.split('\n')]
        return [Drink(int(data[0]), int(data[1]), float(data[2]), float(data[3])) for data in drink_data if data]

    def get_by_id(self, drink_id):
        drinks = self.load()
        for drink in drinks:
            if drink.id == drink_id:
                return drink
        return None

    def load(self):
        loaded_data = super().load()
        print("Loaded Drinks:", loaded_data)
        return loaded_data

class CustomerRepo(DataRepo):
    def convert_to_string(self, customer_list):
        return '\n'.join([f'{customer.id},{customer.name},{customer.address}' for customer in customer_list])

    def convert_from_string(self, content):
        customer_data = [line.split(',') for line in content.split('\n')]
        return [Customer(int(data[0]), data[1], data[2]) for data in customer_data if data]

    def get_by_id(self, customer_id):
        customers = self.load()
        for customer in customers:
            if customer.id == customer_id:
                return customer
        return None

    def get_by_name(self, name):
        customers = self.load()
        for customer in customers:
            if customer.name.lower() == name.lower():
                return customer
        return None

class OrderRepo(DataRepo):
    def convert_to_string(self, order_list):
        return '\n'.join([f'{order.id},{order.customer_id},{",".join(map(str, order.dish_ids))},{",".join(map(str, order.drink_ids))},{order.total_cost}' for order in order_list])

    def convert_from_string(self, content):
        order_data = [line.split(',') for line in content.split('\n')]
        return [Order(int(data[0]), int(data[1]), list(map(int, data[2].split(','))), list(map(int, data[3].split(',')))) for data in order_data if data]

    def get_by_id(self, order_id):
        orders = self.load()
        for order in orders:
            if order.id == order_id:
                return order
        return None
