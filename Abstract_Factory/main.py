from factoria import *
from cliente_factoria import *

if __name__ == "__main__":
    print("Prueba de la factoria 1")
    cliente(Factoria_concreta1())
    print("\n")
    print("Prueba de la factoria 2")
    cliente(Factoria_concreta2())
    