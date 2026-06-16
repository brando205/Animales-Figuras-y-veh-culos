# 1) Animales y sonido:
# Cargamos los componentes necesarios para trabajar con abstracción
from abc import ABC, abstractmethod

# Creamos la clase base abstracta de la que heredarán los animales
class Animal(ABC):
    # Método inicializador para darle nombre a cada instancia
    def __init__(self, nombre):
        self.nombre = nombre  # Guardamos el parámetro en la propiedad de la clase

    # Declaramos el método abstracto para obligar a definir el sonido
    @abstractmethod
    def hacer_sonido(self):
        pass  # Estructura vacía en la clase padre

# Definición de la subclase Perro que hereda de Animal
class Perro(Animal):
    # Retornamos la cadena específica con el ladrido del perro
    def hacer_sonido(self):
        return f"{self.nombre} dice: Guau!"

# Definición de la subclase Gato que hereda de Animal
class Gato(Animal):
    # Retornamos la cadena específica con el maullido del gato
    def hacer_sonido(self):
        return f"{self.nombre} dice: Miau!"

# Definición de la subclase Pajaro que hereda de Animal
class Pajaro(Animal):
    # Retornamos la cadena específica con el canto del ave
    def hacer_sonido(self):
        return f"{self.nombre} dice: Pío pío!"

# Función global para ejecutar el comportamiento polimórfico
def reproducir_sonido(animal: Animal):
    # Polimorfismo: el mismo método actúa diferente según el objeto recibido
    print(animal.hacer_sonido())

# Punto de entrada principal para la ejecución de Python
if __name__ == "__main__":
    # Inicializamos el arreglo con los tres objetos usando los nombres de la hoja
    animales = [
        Perro("Firulais"),
        Gato("Misu"),
        Pajaro("Piolín")
    ]
    
    # Ciclo repetitivo para procesar secuencialmente la lista de animales
    for a in animales:
        reproducir_sonido(a)  # Invocamos la función encargada de imprimir
    