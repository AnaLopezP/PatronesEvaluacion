from abc import ABC, abstractmethod
import csv
import os.path

class PizzaBuilder(ABC):
    
    @property
    @abstractmethod
    def crear_pizza(self):
        pass
    
    @abstractmethod
    def crear_masa(self):
        pass
    
    @abstractmethod
    def crear_salsa(self):
        pass
    
    @abstractmethod
    def crear_ingrediente(self):
        pass
    
    @abstractmethod
    def crear_tecnica(self):
        pass
    
    @abstractmethod
    def crear_presentacion(self):
        pass
    
    @abstractmethod
    def crear_extras(self):
        pass
    
    @abstractmethod
    def crear_bebidas(self):
        pass
    
class Pizza:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.masa = ""
        self.salsa = ""
        self.ingrediente = []
        self.tecnica = ""
        self.presentacion = ""
        self.extras = ""
        self.bebidas = ""
        
    @property
    def pizza(self):
        pizza = [self.masa, self.salsa, self.ingrediente, self.tecnica, self.presentacion, self.extras, self.bebidas]
        self.reset()
        return pizza
    
    def crear_masa(self):
        masa = input("Masa de la pizza: ")        
        self.masa = masa
        
    def crear_salsa(self):
        salsa = input("Salsa de la pizza: ")        
        self.salsa = salsa
    
    def crear_ingrediente(self):
        respuesta = "si"
        while respuesta == "si":
            ingrediente = input("Ingrediente de la pizza: ")        
            self.ingrediente.append(ingrediente)
            respuesta = input("Desea agregar otro ingrediente? si/no: ")
    
    def crear_tecnica(self):
        tecnica = input("Tecnica de la pizza: ")        
        self.tecnica = tecnica
        
    def crear_presentacion(self):
        presentacion = input("Presentacion de la pizza: ")        
        self.presentacion = presentacion
    
    def crear_extras(self):
        extras = input("Extras de la pizza: ")        
        self.extras = extras
    
    def crear_bebidas(self):
        bebidas = input("Bebida con la pizza: ")        
        self.bebidas = bebidas
        
class Producto():
    def __init__(self):
        self._pizza = []
        
    def add(self, parte):
        self._pizza.append(parte)
        
    def __str__(self):
        return f"Partes de la pizza: {', '.join(self._pizza)}"        
        

class CSV_Builder():
    def crear_csv(self):
        with open('pizza.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Masa", "Salsa", "Ingrediente", "Tecnica", "Presentacion", "Extras", "Bebidas"])
        file.close()
        
    def añadir_pizza(self):
        with open('pizza.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([pizza[0], pizza[1], pizza[2], pizza[3], pizza[4], pizza[5], pizza[6]])
        file.close()

class PizzaDirector:
    def __init__(self, builder):
        self._builder = builder
        
    def crear_pizza(self):
        self._builder.crear_masa()
        self._builder.crear_salsa()
        self._builder.crear_ingrediente()
        self._builder.crear_tecnica()
        self._builder.crear_presentacion()
        self._builder.crear_extras()
        self._builder.crear_bebidas()
        
    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self, builder):
        self._builder = builder

if __name__ == "__main__":
    print("Creando constructor de pizza...")
    builder = Pizza()
    print("Trayendo al camarero...")
    print("¡Benvenido a la Pizzeria AnaLaRana! Por favor, siga los pasos para crear su pizza. Tenemos TODO lo que se pueda imaginar:")
    director = PizzaDirector(builder)
    director.crear_pizza()
    pizza = builder.pizza
    print(pizza)
    respuesta = input("¿Quiere pedir otra pizza?si/no: ")
    while respuesta == "si":
        director.crear_pizza()
        pizza = builder.pizza
        print(pizza)
        respuesta = input("¿Quiere pedir otra pizza?si/no: ")
    print("Gracias por su visita. ¡Que aproveche! (en la pizzería AnaLaRana no nos hacemos responsables de enfermedades estomacales ni de intoxicaciones alimentecias. Todo lo que pida el cliente es bajo su responsabilidad.)")
    
    csv_builder = CSV_Builder()
    if not os.path.isfile('pizza.csv'):
        csv_builder.crear_csv()
    csv_builder.añadir_pizza()
