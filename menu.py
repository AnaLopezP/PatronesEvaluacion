import Abstract_Factory.main as AF
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
            AF.main()

        if decision == 2:
            df = pd.read_csv('pokemon.csv')
            lista = []
            for i in df.iloc:
                dicc = {}
                dicc['Nombre'] = i['Name']
                dicc['Tipo 1'] = i['Type 1']
                dicc['Tipo 2'] = i['Type 2']
                dicc['Numero'] = i['#']
                lista.append(dicc)
            a1_numero = arbol_pokemon.nodoArbol(lista[0])
            a2_nombre = arbol_pokemon.nodoArbol(lista[0])
            a3_tipo = arbol_pokemon.nodoArbol(lista[0])
            Ejercicio2.crear_arbol(a1_numero, 'Numero', lista)
            Ejercicio2.crear_arbol(a2_nombre, 'Nombre', lista)
            Ejercicio2.crear_arbol(a3_tipo, 'Tipo 1', lista)

            numero_2 = []
            a1_numero.buscar_xnumero(2, numero_2)

            nombre = []
            a2_nombre.buscar_bien('h', nombre)

            tipo_fuego = []
            a3_tipo.buscar_xtipo('Fire', tipo_fuego)
            print('-----------------------POKEMONS TIPO FUEGO---------------------------')
            print(tipo_fuego)

            tipo_electro = []
            a3_tipo.buscar_xtipo('Electric', tipo_electro)
            print('-------------------POKEMONS TIPO ELECTRO---------------------')
            print(tipo_electro)

            tipo_agua = []
            a3_tipo.buscar_xtipo('Water', tipo_agua)
            print('-------------------POKEMONS TIPO AGUA---------------------')
            print(tipo_agua)

            tipo_planta = []
            a3_tipo.buscar_xtipo('Grass', tipo_planta)
            print('-------------------POKEMONS TIPO PLANTA---------------------')
            print(tipo_planta)

            print('Los pokemons que son débiles a Jolteon son aquellos de tipo: agua y volador')
            print('\n')
            deb_jolteon = []
            a3_tipo.buscar_xtipo('Water', deb_jolteon)
            a3_tipo.buscar_xtipo('Flying', deb_jolteon)
            print(deb_jolteon)
            print('\n')
            print('Los pokemons débiles a Lycanroc son los de tipo: Bicho, fuego, hielo y volador')
            print('\n')
            deb_lycanroc = []
            a3_tipo.buscar_xtipo('Bug', deb_lycanroc)
            a3_tipo.buscar_xtipo('Fire', deb_lycanroc)
            a3_tipo.buscar_xtipo('Ice', deb_lycanroc)
            a3_tipo.buscar_xtipo('Flying', deb_lycanroc)
            print(deb_lycanroc)
            print('\n')
            print('Como Tyrantrum es de tipo roca y dragón, es fuerte contra los mismos que Lycanroc más los que son débiles contra tipo dragón, que es el tipo dragón')
            print('\n')
            deb_tyrantrum = deb_lycanroc
            a3_tipo.buscar_xtipo('Dragon', deb_tyrantrum)
            print(deb_tyrantrum)
            print('\n')
            tipos = []
            a3_tipo.tipos(tipos)
            print('--------------------TIPOS DE POKEMONS---------------------')
            print(tipos)

            for i in tipos:
                todos = []
                a3_tipo.buscar_xtipo(i, todos)
                print('\n')
                print('NUMERO DE POKEMONS TIPO: ' + str(i))
                print(len(todos))

            print('-----------------------------POKEMONS ORDENADOS POR NUMERO DE MANERA ASCENDENTE--------------------------')
            listanum = []
            a1_numero.ordenascendente(listanum)
            for i in range(0, 5):
               print(listanum[i])
            print('\n')
            print('---------------------------POKEMONS ORDENADOS POR NOMBRE ASCENDENTE------------------------------')
            listanombre = []
            a2_nombre.ordenascendente(listanombre)
            for i in range(0, 5):
                print(listanombre[i])

            print('\n')
            print('---------------------------------POKEMONS ORDENADOS POR NIVEL POR NOMBRE----------------------')
            nombrenivel = []
            a2_nombre.por_nivel(nombrenivel)
            for i in range(0, 5):
                print(nombrenivel[i])

        if decision == 3:
            print('-----------------------DATOS 7 MARAVILLAS--------------------------')
            print('Muralla China, en China, tipo arquitectonico')
            print('Petra, en Jordania, tipo arquitectonico')
            print('Coliseo, en Italia, tipo arquitectonico')
            print('Chichen Izta, en Mexico, tipo arquitectonico')
            print('Gran Cañon, en EEUU, tipo natural')
            print('Cristo Redentor, en Brasil, tipo arquitectonico')
            print('Taj Mahal, en India, tipo arquitectonico')
            print('\n')
            grafo = Ejercicio3.iniciarDatos()
            grafo.pintar()
            Ejercicio3.resetVisitados(grafo)
            Ejercicio3.relacionar(grafo)
            print('-----------------------------------------------')
            Ejercicio3.resetVisitados(grafo)
            grafo.pintar()
            Ejercicio3.resetVisitados(grafo)

            lista = Ejercicio3.ListaCatalogo()
            Ejercicio3.juntarDatosPaises(grafo, lista)
            if (lista.paisConDos()):
                print("Existe un pais con dos tipos de maravillas")
            else :
                print("NO Existe un pais con dos tipos de maravillas")

            if (lista.paisConDosDeUnTipo()):
                print("Existe un pais con dos maravillas del mismo tipo")
            else :
                print("NO Existe un pais con dos maravillas del mismo tipo")

        if decision == 4:
            print('Saliendo')
            break

        input("\nPresiona ENTER  para continuar")
iniciar()