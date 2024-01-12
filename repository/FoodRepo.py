from repository.DataRepo import DataRepo
from modelle.GekochterGericht import GekochterGericht

def getObject(list):
    object = GekochterGericht(list[0],list[1],list[2],list[3],list[4])
    return object

class FoodRepo(DataRepo):
    def __init__(self, datei):
        super().__init__(datei)

    def convert_to_string(self, objects):
        lines = list(map(self.getString,objects))
        return lines

    def convert_from_string(self, lines):
        objects = list(map(getObject,lines))
        return objects


