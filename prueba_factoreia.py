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
    
    
#clase de un producto abstracto grtafica 2
class Grafica_2(ABC):
    @abstractmethod
    def mostrar(self):
        pass

#clase de un producto abstracto analisis 1
class Analisis_1(ABC):
    @abstractmethod
    def mostrar(self):
        pass

#clase de un producto abstracto analisis 2
class Analisis_2(ABC):
    @abstractmethod
    def mostrar(self):
        pass
    

#clase de un producto concreto grafica 1
class grafica1_concreta1(Grafica_1):
    def mostrar(self):
        print("Grafica 1 tipo 1")
        
#clase de un producto concreto grafica 1
class grafica1_concreta2(Grafica_1):
    def mostrar(self):
        print("Grafica 1 tipo 2")
        
#clase de un producto concreto grtafica 2
class grafica2_concreta1(Grafica_2):
    def mostrar(self):
        print("Grafica 2 tipo 1")
        
class grafica2_concreta2(Grafica_2):
    def mostrar(self):
        print("Grafica 2 tipo 2")
        
#clase de un producto concreto analisis 1
class analisis1_concreta1(Analisis_1):
    def mostrar(self):
        print("Analisis 1 tipo 1")
class analisis1_concreta2(Analisis_1):
    def mostrar(self):
        print("Analisis 1 tipo 2")
              
#clase de un producto concreto analisis 2
class analisis2_concreta1(Analisis_2):
    def mostrar(self):
        print("Analisis 2")
        
class analisis2_concreta2(Analisis_2):
    def mostrar(self):
        print("Analisis 2")
        
        