# data_repo.py
import pickle
import modelle

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
        pass

    def convert_from_string(self, content):
        pass

    def get_by_id(self, obj_id):
        for obj in self.load():
            if hasattr(obj, 'id') and obj.id == obj_id:
                return obj
        return None
