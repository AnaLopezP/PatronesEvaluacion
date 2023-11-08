from Abstract_Factory import main, factoria, cliente_factoria, lectura_csv
import Pizzeria_builder.main as Pizzeria_builder_main
import helpers

def iniciar():
    while True:
        helpers.limpiar_pantalla()
        
        print("QUE EJERCICIO QUIERES VER:")
        print("[1] Ejercicio 1: Abstract Factory")
        print("[2] Ejercicio 2: Pizzeria AnaLaRana Builder")
        print("[3] Ninguno")

        decision = int(input("> "))
        helpers.limpiar_pantalla()
        if decision == 1:
            print("Ejercicio 1: Abstract Factory")
            main.main()

        if decision == 2:
            print("Ejercicio 2: Pizzeria AnaLaRana Builder")
            Pizzeria_builder_main.main()

        if decision == 3:
            print('Saliendo')
            break

        input("\nPresiona ENTER  para continuar")
iniciar()