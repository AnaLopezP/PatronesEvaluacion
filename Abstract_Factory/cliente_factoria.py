from . import factoria
from . import lectura_csv
#funcion cliente que recibe una factoria
def cliente(factory: factoria.Analisis_datos_factory):
    grafica = factory.crear_grafica()
    analisis = factory.crear_analisis()
    grafica.mostrar(lectura_csv.data)
    analisis.mostrar(lectura_csv.data)
    