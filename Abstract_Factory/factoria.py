from abc import ABC, abstractmethod
from pandas import *
import matplotlib.pyplot as plt
from . import lectura_csv


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
    
    
    
#clase de un producto abstracto grafica 
class Grafica(ABC):
    @abstractmethod
    def mostrar(self):
        pass
    
    
#clase de un producto abstracto analisis
class Analisis(ABC):
    @abstractmethod
    def mostrar(self):
        pass

#clase de un producto concreto grafica de barras
class grafica_debarras(Grafica):
    def mostrar(self, data):
        data['FECHA'] = to_datetime(data['FECHA']) #transformamos los datos en formato fecha
        data['MES'] = data['FECHA'].dt.month #cogemos los meses de cada dato
        activaciones_por_mes = data['MES'].value_counts().sort_index() #contamos los meses que hay activaciones y los ordenamos
        #hacemos la gráfica
        activaciones_por_mes.plot(kind='bar', color="skyblue", edgecolor="black")
        plt.title("Activaciones por mes")
        plt.show()
        
#clase de un producto concreto grafica histograma
class grafica_histograma(Grafica):
    def mostrar(self, data):
        activaciones_por_tipo = data['TITULO'].value_counts() #contamos los tipos de activaciones
        #hacemos la gráfica
        activaciones_por_tipo.plot(kind='bar', color="skyblue", edgecolor="black")
        plt.title("Historiograma de activaciones por tipo de emergencia")
        plt.show()

#clase de un producto concreto analisis media
class analisis_media(Analisis):
    def mostrar(self, data):
        data['FECHA'] = to_datetime(data['FECHA']) #transformamos los datos en formato fecha
        data['DÍA'] = data['FECHA'].dt.day #cogemos los dias de cada dato
        activaciones_por_dia = data['DÍA'].value_counts().sort_index() #contamos los dias que hay activaciones y los ordenamos
        #printeamos y devolvemos la media
        print("Media de activaciones por dia: " + str(activaciones_por_dia.mean()))
        return activaciones_por_dia.mean()

#clase de un producto concreto analisis mediana
class analisis1_mediana(Analisis):
    def mostrar(self, data):
        #hacemos lo mismo para la mediana
        data['FECHA'] = to_datetime(data['FECHA'])
        data['DÍA'] = data['FECHA'].dt.day
        activaciones_por_dia = data['DÍA'].value_counts().sort_index()
        print("Mediana de activaciones por dia: " + str(activaciones_por_dia.median()))
        return activaciones_por_dia.median()
              
