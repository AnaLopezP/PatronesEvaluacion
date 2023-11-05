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
class Factoria_concreta1(Analisis_datos_factory):
    @abstractmethod
    def crear_grafica(self):
        return grafica_debarras()
    
    @abstractmethod
    def crear_analisis(self):
        return analisis1_mediana()
    
#clase de una factoria concreta
class Factoria_concreta2(Analisis_datos_factory):
    @abstractmethod
    def crear_grafica(self):
        return grafica_histograma()
    
    @abstractmethod
    def crear_analisis(self):
        return analisis_media()
    
    
    
#clase de un producto abstracto grafica 1
class Grafica(ABC):
    @abstractmethod
    def mostrar(self):
        pass
    
    
'''#clase de un producto abstracto grtafica 2
class Grafica_historiograma(ABC):
    @abstractmethod
    def mostrar(self):
        pass'''

#clase de un producto abstracto analisis 1
class Analisis(ABC):
    @abstractmethod
    def mostrar(self):
        pass
'''
#clase de un producto abstracto analisis 2
class Analisis_2(ABC):
    @abstractmethod
    def mostrar(self):
        pass
    '''

#clase de un producto concreto grafica 1
class grafica_debarras(Grafica):
    def mostrar(self):
        print("Grafica barras")
        
#clase de un producto concreto grafica 1
class grafica_histograma(Grafica):
    def mostrar(self):
        print("Grafica histograma")
        
'''#clase de un producto concreto grtafica 2
class grafica2_concreta1(Grafica_historiograma):
    def mostrar(self):
        print("Grafica historiograma tipo 1")
        
class grafica2_concreta2(Grafica_historiograma):
    def mostrar(self):
        print("Grafica 2 tipo 2")
        '''
#clase de un producto concreto analisis 1
class analisis_media(Analisis):
    def mostrar(self):
        print("Analisis media")
        
class analisis1_mediana(Analisis):
    def mostrar(self):
        print("Analisis mediana")
              
'''class analisis_moda(Analisis):
    def mostrar(self):
        print("Analisis moda")'''
        
'''class analisis2_concreta2(Analisis_2):
    def mostrar(self):
        print("Analisis 2")'''
        
def cliente(factory: Analisis_datos_factory):
    grafica = factory.crear_grafica()
    analisis = factory.crear_analisis()
    grafica.mostrar()
    analisis.mostrar()