from abc import ABC,ABCMeta,abstractmethod
import pickle

class DataRepo(ABC):
    @abstractmethod
    def __init__(self,datei):
        self.datei = datei

    def getString(self, object):
        # Wie order ausschauen muss
        desired_order = ['id', 'name', 'portionsgrosse', 'preis', 'zubereitungszeit', 'alkoholgehalt', 'name', 'adresse']

        # Alle Attribute der Objekte, die nicht mit _ beginnen oder Methoden sidnd
        attributes = {attr: getattr(object, attr) for attr in dir(object)
                      if not callable(getattr(object, attr)) and not attr.startswith('_')}

        # Sortierung der Attribute in der gewunschten Reihenfolge
        sorted_attributes = sorted(attributes.items(),
                                   key=lambda x: desired_order.index(x[0]) if x[0] in desired_order else len(
                                       desired_order))

        # Format un return der Attribute
        return [f'{key}: {str(value)}' for key, value in sorted_attributes]

    def save(self,objects):
        with open(self.datei,'wb') as file:
            pickle.dump(objects,file)

    def load(self):
        with open(self.datei,'rb') as file:
            objects = pickle.load(file)
        return objects

    def read_file(self):
        content = []
        with open(self.datei,'r') as file:
            for line in file:
                content.append(line.strip())
        return content

    def write_to_file(self,content):
        with open(self.datei,'w') as file:
            for line in content:
                file.write(line + '\n')


    def convert_to_string(self):
        pass

    def convert_from_string(self):
        pass

