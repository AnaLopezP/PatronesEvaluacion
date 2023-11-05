from abc import ABC, abstractmethod
import csv

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
        self._pizza = Producto()
        
    @property
    def pizza(self):
        pizza = self._pizza
        self.reset()
        return pizza
    
    def crear_masa(self):
        masa = input("Masa de la pizza: ")        
        self._pizza.add(masa)
        
    def crear_salsa(self):
        salsa = input("Salsa de la pizza: ")        
        self._pizza.add(salsa)
    
    def crear_ingrediente(self):
        respuesta = "si"
        while respuesta == "si":
            ingrediente = input("Ingrediente de la pizza: ")        
            self._pizza.add(ingrediente)
            respuesta = input("Desea agregar otro ingrediente? si/no: ")
    
    def crear_tecnica(self):
        tecnica = input("Tecnica de la pizza: ")        
        self._pizza.add(tecnica)
        
    def crear_presentacion(self):
        presentacion = input("Presentacion de la pizza: ")        
        self._pizza.add(presentacion)
    
    def crear_extras(self):
        extras = input("Extras de la pizza: ")        
        self._pizza.add(extras)
    
    def crear_bebidas(self):
        bebidas = input("Bebida con la pizza: ")        
        self._pizza.add(bebidas)
        
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
            writer.writerow([self._pizza.masa, self._pizza.salsa, self._pizza.ingrediente, self._pizza.tecnica, self._pizza.presentacion, self._pizza.extras, self._pizza.bebidas])
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
    director = PizzaDirector(builder)
    director.crear_pizza()
    pizza = builder.pizza
    print(pizza)
    
    csv_builder = CSV_Builder()
    csv_builder.crear_csv()
    csv_builder.añadir_pizza()