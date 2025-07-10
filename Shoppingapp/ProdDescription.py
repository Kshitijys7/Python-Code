from abc import ABC,abstractmethod
class ProdDescription(ABC):
    @abstractmethod
    def description(self):
        pass