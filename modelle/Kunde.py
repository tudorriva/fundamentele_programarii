from modelle.Identifizierbar import Identifizierbar

class Kunde(Identifizierbar):
    def __init__(self,id,name,adresse):
        super().__init__(id)
        self.name = name
        self.adresse = adresse