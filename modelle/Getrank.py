from modelle.Gericht import Gericht

class Getrank(Gericht):
    def __init__(self,id,name,portionsgrosse,preis,alkoholgehalt):
        super().__init__(id,name,portionsgrosse,preis)
        self.alkoholgehalt = alkoholgehalt


