from abc import ABC, abstractmethod

class Analisis_datos_factory(ABC):
    @abstractmethod
    def crear_grafica(self):
        pass

    @abstractmethod
    def crear_analisis(self):
        pass
    
class Grafica(Analisis_datos_factory):
    @abstractmethod
    def crear_grafica_1(self):
        pass
    
    @abstractmethod
    def crear_grafica_2(self):
        pass
    
class Analisis(Analisis_datos_factory):
    @abstractmethod
    def crear_analisis_1(self):
        pass
    
    @abstractmethod
    def crear_analisis_2(self):
        pass