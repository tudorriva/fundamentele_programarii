from abc import ABC,ABCMeta,abstractmethod
class Identifizierbar(ABC):
    @abstractmethod
    def __init__(self,id):
        self.id = id


