from . import factoria, cliente_factoria

def main():
    print("Prueba de la factoria 1")
    cliente_factoria.cliente(factoria.Factoria_concreta1())
    print("\n")
    print("Prueba de la factoria 2")
    cliente_factoria.cliente(factoria.Factoria_concreta2())
    
if __name__ == "__main__":
    main()