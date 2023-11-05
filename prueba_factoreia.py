from abc import ABC, abstractmethod

#clase de la abstract factory
class Analisis_datos_factory(ABC):
    @abstractmethod
    def crear_grafica(self):
        pass

    @abstractmethod
    def crear_analisis(self):
        pass

#clase de una factoria concreta
class Grafica(Analisis_datos_factory):
    @abstractmethod
    def crear_grafica_1(self):
        pass
    
    @abstractmethod
    def crear_grafica_2(self):
        pass
    
#clase de una factoria concreta
class Analisis(Analisis_datos_factory):
    @abstractmethod
    def crear_analisis_1(self):
        pass
    
    @abstractmethod
    def crear_analisis_2(self):
        pass
    
#clase de un producto abstracto grtafica 1
class Grafica_1(ABC):
    @abstractmethod
    def mostrar(self):
        pass
    
class Grafica_2(ABC):
    @abstractmethod
    def mostrar(self):
        pass