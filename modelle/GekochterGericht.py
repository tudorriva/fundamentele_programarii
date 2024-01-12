from modelle.Gericht import Gericht


class GekochterGericht(Gericht):
    def __init__(self,id,name,portionsgrosse,preis,zubereitungszeit):
        super().__init__(id,name,portionsgrosse,preis)
        self.zubereitungszeit = zubereitungszeit

