from Abstract_Factory import main, factoria, cliente_factoria, lectura_csv
import Pizzeria_builder.pizzeria_AnaLaRana as Pizzeria_builder



def iniciar():
    while True:

        print("QUE EJERCICIO QUIERES VER:")
        print("[1] Ejercicio 1: Abstract Factory")
        print("[2] Ejercicio 2: Pizzeria AnaLaRana Builder")
        print("[3] Ninguno")

        decision = int(input("> "))
        if decision == 1:
            print("Ejercicio 1: Abstract Factory")
            main.main()

        if decision == 2:
            print("Ejercicio 2: Pizzeria AnaLaRana Builder")
            Pizzeria_builder.main()

        if decision == 3:
            print('Saliendo')
            break

        input("\nPresiona ENTER  para continuar")
iniciar()