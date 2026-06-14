# PRÁCTICA 1: DEMOSTRACIÓN DE POLIMORFISMO CON ANIMALES

# Traemos las herramientas necesarias para manejar el modelo abstracto
from abc import ABC, abstractmethod

# Creamos la clase padre llamada Animal
class Animal(ABC):
    # Con este método registramos el nombre de cada mascota
    def __init__(self, nombre_mascota):
        self.nombre = nombre_mascota

    # Definimos la regla de que todo animal debe hacer ruido
    @abstractmethod
    def hacer_sonido(self):
        pass  # Se queda vacío porque cada hijo tendrá su propio ruido

# Primera clase hija: El Perro
class Perro(Animal):
    # Personalizamos el ruido del perro
    def hacer_sonido(self):
        return f"El perro {self.nombre} ladra: ¡Guau guau!"

# Segunda clase hija: El Gato
class Gato(Animal):
    # Personalizamos el ruido del gato
    def hacer_sonido(self):
        return f"El gato {self.nombre} maúlla: ¡Miau miau!"

# Tercera clase hija: El Pájaro
class Pajaro(Animal):
    # Personalizamos el ruido del ave
    def hacer_sonido(self):
        return f"El ave {self.nombre} canta: ¡Pío pío!"

# Esta función se encarga de ejecutar el polimorfismo en la terminal
def activar_voz_animal(objeto_animal):
    # Ejecuta el sonido que le corresponde a la subclase
    print(objeto_animal.hacer_sonido())

# Punto de inicio de nuestra aplicación
if __name__ == "__main__":
    # Creamos un grupo con tres mascotas diferentes
    lista_mascotas = [
        Perro("Rocky"),
        Gato("Luna"),
        Pajaro("Paco")
    ]

    # Mandamos a llamar la función para cada uno de forma automática
    for mascota in lista_mascotas:
        activar_voz_animal(mascota)