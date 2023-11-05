from factoria import *

#funcion cliente que recibe una factoria
def cliente(factory: Analisis_datos_factory):
    grafica = factory.crear_grafica()
    analisis = factory.crear_analisis()
    grafica.mostrar(data)
    analisis.mostrar(data)
    