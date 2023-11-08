from . import pizzeria_AnaLaRana
import os
def main():
    print("Creando constructor de pizza...")
    builder = pizzeria_AnaLaRana.Pizza()
    print("Trayendo al camarero...")
    print("¡Benvenido a la Pizzeria AnaLaRana! Por favor, siga los pasos para crear su pizza. Tenemos TODO lo que se pueda imaginar (sin juzgar, todos tenemos gustos):")
    director = pizzeria_AnaLaRana.PizzaDirector(builder)
    director.crear_pizza()
    pizza = builder.pizza
    print(pizza)
    respuesta = input("¿Quiere pedir otra pizza?si/no: ")
    csv_builder = pizzeria_AnaLaRana.CSV_Builder()
    while respuesta == "si":
        director.crear_pizza()
        pizza = builder.pizza
        print(pizza)
        respuesta = input("¿Quiere pedir otra pizza?si/no: ")
        if not os.path.isfile('pizza.csv'):
            csv_builder.crear_csv()
        csv_builder.añadir_pizza(pizza)
    print("Gracias por su visita. ¡Que aproveche! (en la pizzería AnaLaRana no nos hacemos responsables de enfermedades estomacales ni de intoxicaciones alimentecias. Todo lo que pida el cliente es bajo su responsabilidad.)")
    
    

if __name__ == "__main__":
    main()