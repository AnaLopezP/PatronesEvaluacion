from abc import ABC, abstractmethod
from pandas import *
import matplotlib.pyplot as plt
from lectura_csv import data


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
        data['FECHA'] = to_datetime(data['FECHA'])
        data['MES'] = data['FECHA'].dt.month
        activaciones_por_mes = data['MES'].value_counts().sort_index()
        activaciones_por_mes.plot(kind='bar', color="skyblue", edgecolor="black")
        plt.title("Activaciones por mes")
        plt.show()
        
#clase de un producto concreto grafica 1
class grafica_histograma(Grafica):
    def mostrar(self, data):
        activaciones_por_tipo = data['TITULO'].value_counts()
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
    def mostrar(self, data):
        data['FECHA'] = to_datetime(data['FECHA'])
        data['DÍA'] = data['FECHA'].dt.day
        activaciones_por_dia = data['DÍA'].value_counts().sort_index()
        print("Media de activaciones por dia: " + str(activaciones_por_dia.mean()))
        return activaciones_por_dia.mean()
        
class analisis1_mediana(Analisis):
    def mostrar(self, data):
        data['FECHA'] = to_datetime(data['FECHA'])
        data['DÍA'] = data['FECHA'].dt.day
        activaciones_por_dia = data['DÍA'].value_counts().sort_index()
        print("Mediana de activaciones por dia: " + str(activaciones_por_dia.median()))
        return activaciones_por_dia.median()
              
'''class analisis_moda(Analisis):
    def mostrar(self):
        print("Analisis moda")'''
        
'''class analisis2_concreta2(Analisis_2):
    def mostrar(self):
        print("Analisis 2")'''
        
def cliente(factory: Analisis_datos_factory):
    grafica = factory.crear_grafica()
    analisis = factory.crear_analisis()
    grafica.mostrar(data)
    analisis.mostrar(data)
    

if __name__ == "__main__":
    print("Prueba de la factoria 1")
    cliente(Factoria_concreta1())
    print("\n")
    print("Prueba de la factoria 2")
    cliente(Factoria_concreta2())
    