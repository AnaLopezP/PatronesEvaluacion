from abc import ABC, abstractmethod
from pandas import *
import matplotlib.pyplot as plt
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
    def crear_grafica(self):
        return grafica_debarras()
    
    def crear_analisis(self):
        return analisis1_mediana()
    
#clase de una factoria concreta
class Factoria_concreta2(Analisis_datos_factory):
    def crear_grafica(self):
        return grafica_histograma()
    
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
    def mostrar(self, data):
        data['FECHA_ACTIVACION'] = to_datetime(data['FECHA_ACTIVACION'])
        data['MES'] = data['FECHA_ACTIVACION'].dt.month
        activaciones_por_mes = data['MES'].value_counts().sort_index()
        activaciones_por_mes.plot(kind='bar', color="skyblue", edgecolor="black")
        plt.title("Activaciones por mes")
        plt.show()
        
#clase de un producto concreto grafica 1
class grafica_histograma(Grafica):
    def mostrar(self, data):
        activaciones_por_tipo = data['TIPO_EMERGENCIA'].value_counts()
        activaciones_por_tipo.plot(kind='bar', color="skyblue", edgecolor="black")
        plt.title("Historiograma de activaciones por tipo de emergencia")
        plt.show()
        
'''#clase de un producto concreto grtafica 2
class grafica2_concreta1(Grafica_historiograma):
    def mostrar(self):
        print("Grafica historiograma tipo 1")
        
class grafica2_concreta2(Grafica_historiograma):
    def mostrar(self):
        print("Grafica 2 tipo 2")
        '''
#clase de un producto concreto
class analisis_media(Analisis):
    def mostrar(self, datos, columna):
        return datos[columna].mean()
        
class analisis1_mediana(Analisis):
    def mostrar(self, datos, columna):
        return datos[columna].median()
              
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
    

if __name__ == "__main__":
    print("Prueba de la factoria 1")
    cliente(Factoria_concreta1())
    print("\n")
    print("Prueba de la factoria 2")
    cliente(Factoria_concreta2())
    