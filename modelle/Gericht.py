from modelle.Identifizierbar import Identifizierbar
from abc import ABC,ABCMeta,abstractmethod

class Gericht(Identifizierbar):
    def __init__(self,id,name,portionsgrosse,preis):
        super().__init__(id)
        self.name = name
        self.portionsgrosse = portionsgrosse
        self.preis = preis


