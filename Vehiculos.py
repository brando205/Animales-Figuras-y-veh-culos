# 3) Vehículos y movimientos:

# Cargamos los módulos necesarios para implementar la abstracción en Python
from abc import ABC, abstractmethod

# Clase base abstracta que sirve como plantilla general para los transportes
class Vehiculo(ABC):
    # Constructor que inicializa cada objeto asignándole una marca de fábrica
    def __init__(self, marca: str):
        self.marca = marca  

    # Regla obligatoria: cada subclase debe definir su método de arranque
    @abstractmethod
    def arrancar(self):
        pass

    # Regla obligatoria: cada subclase debe definir su método de desplazamiento
    @abstractmethod
    def moverse(self):
        pass

# Primera clase derivada: representa a un automóvil común
class Auto(Vehiculo):
    # Definición de la acción de encendido específica para el auto
    def arrancar(self):
        print(f"Auto {self.marca} arrancando con llave.")

    # Definición del tipo de movimiento que realiza el auto en carretera
    def moverse(self):
        print(f"Auto {self.marca} circulando por la carretera.")

# Segunda clase derivada: representa a una motocicleta
class Moto(Vehiculo):
    # Definición de la acción de encendido específica para la moto
    def arrancar(self):
        print(f"Moto {self.marca} arrancando con botón eléctrico.")

    # Definición del tipo de movimiento que realiza la moto entre el tráfico
    def moverse(self):
        print(f"Moto {self.marca} avanzando entre el tráfico.")

# Tercera clase derivada: representa a un camión de carga pesada
class Camion(Vehiculo):
    # Definición de la acción de encendido específica para el camión
    def arrancar(self):
        print(f"Camión {self.marca} encendiendo motor diésel.")

    # Definición del tipo de movimiento que realiza el camión con su mercancía
    def moverse(self):
        print(f"Camión {self.marca} transportando carga pesada.")

# Función global polimórfica que opera cualquier tipo de vehículo registrado
def iniciar_viaje(vehiculo: Vehiculo):
    # Ejecuta el arranque y el movimiento sin importar qué transporte sea
    vehiculo.arrancar()
    vehiculo.moverse()

# Bloque de arranque principal del entorno de Python
if __name__ == "__main__":
    # Creación del arreglo 'flota' con los modelos exactos indicados por el profesor
    flota = [
        Auto("Toyota"),
        Moto("Yamaha"),
        Camion("Volvo")
    ]
    
    # Recorremos la flotilla de vehículos de forma automática usando el ciclo for
    for v in flota:
        iniciar_viaje(v)
        # Imprime la línea divisoria de guiones después de cada transporte
        print("-" * 20)