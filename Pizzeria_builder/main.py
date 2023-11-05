from pizzeria_AnaLaRana import *
if __name__ == "__main__":
    print("Creando constructor de pizza...")
    builder = Pizza()
    print("Trayendo al camarero...")
    print("¡Benvenido a la Pizzeria AnaLaRana! Por favor, siga los pasos para crear su pizza. Tenemos TODO lo que se pueda imaginar:")
    director = PizzaDirector(builder)
    director.crear_pizza()
    pizza = builder.pizza
    print(pizza)
    
    
    if not os.path.isfile('pizza.csv'):
        csv_builder = CSV_Builder()
        csv_builder.crear_csv()
    csv_builder.añadir_pizza()