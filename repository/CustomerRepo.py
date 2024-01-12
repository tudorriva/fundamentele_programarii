from repository.DataRepo import DataRepo
from modelle.Kunde import Kunde
def getObject(string):
    object = Kunde(string[0],string[1],string[2])
    return object

class CustomerRepo(DataRepo):
    def __init__(self, datei):
        super().__init__(datei)

    def convert_to_string(self, objects):
        lines = list(map(self.getString,objects))
        return lines

    def convert_from_string(self, lines):
        objects = list(map(getObject,lines))
        return objects