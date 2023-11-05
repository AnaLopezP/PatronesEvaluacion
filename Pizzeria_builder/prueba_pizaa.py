from abc import ABC, abstractmethod

class PizzaBuilder(ABC):
    
    @property
    @abstractmethod
    def crear_pizza(self):
        pass
    
    @abstractmethod
    def crear_masa(self):
        pass
    
    @abstractmethod
    def crear_salsa(self):
        pass
    
    @abstractmethod
    def crear_ingrediente(self):
        pass
    
    @abstractmethod
    def crear_tecnica(self):
        pass
    
    @abstractmethod
    def crear_presentacion(self):
        pass
    
    @abstractmethod
    def crear_extras(self):
        pass
    
    @abstractmethod
    def crear_bebidas(self):
        pass
    
class 