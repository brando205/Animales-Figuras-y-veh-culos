# 3) Vehículos y movimientos:
# Importamos las herramientas nativas para implementar la herencia abstracta
from abc import ABC, abstractmethod

# Creamos el molde principal denominado Vehiculo
class Vehiculo(ABC):
    # El constructor recibe la marca técnica del transporte actual
    def __init__(self, marca: str):
        self.marca = marca  # Registramos el dato dentro de la instancia

    # Exigimos que todas las clases derivadas implementen un encendido
    @abstractmethod
    def arrancar(self):
        pass

    # Exigimos que todas las clases derivadas implementen un desplazamiento
    @abstractmethod
    def moverse(self):
        pass

# Clase derivada que define el comportamiento para un Auto convencional
class Auto(Vehiculo):
    # Mostramos el mensaje informativo sobre cómo enciende el coche
    def arrancar(self):
        print(f"Auto {self.marca} arrancando con llave.")

    # Mostramos el mensaje informativo sobre dónde avanza el coche
    def moverse(self):
        print(f"Auto {self.marca} circulando por la carretera.")

# Clase derivada que define el comportamiento para una Motocicleta
class Moto(Vehiculo):
    # Mostramos el mensaje informativo sobre cómo enciende la motocicleta
    def arrancar(self):
        print(f"Moto {self.marca} arrancando con botón eléctrico.")

    # Mostramos el mensaje informativo sobre dónde avanza la motocicleta
    def moverse(self):
        print(f"Moto {self.marca} avanzando entre el tráfico.")

# Clase derivada que define el comportamiento para un Camión comercial
class Camion(Vehiculo):
    # Mostramos el mensaje informativo sobre cómo enciende el transporte pesado
    def arrancar(self):
        print(f"Camión {self.marca} encendiendo motor diésel.")

    # Mostramos el mensaje informativo sobre dónde avanza el transporte pesado
    def moverse(self):
        print(f"Camión {self.marca} transportando carga pesada.")

# Función externa diseñada para operar bajo el principio de polimorfismo
def iniciar_viaje(vehiculo: Vehiculo):
    # Se ejecutan los métodos comunes definidos en la estructura base
    vehiculo.arrancar()
    vehiculo.moverse()

# Comprobación del entorno principal de ejecución de Python
if __name__ == "__main__":
    # Agrupamos los elementos dentro de la lista denominada 'flota'
    flota = [
        Auto("Toyota"),
        Moto("Yamaha"),
        Camion("Volvo")
    ]
    
    # Estructura cíclica para iterar sobre cada medio de transporte disponible
    for v in flota:
        iniciar_viaje(v)      # Pasamos el objeto actual a la función operativa
        print("-" * 20)       # Línea divisoria para separar los bloques de texto