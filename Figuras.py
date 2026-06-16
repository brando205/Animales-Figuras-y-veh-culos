# 2) Figuras geométricas (área)
# Cargamos los módulos que nos permiten definir estructuras abstractas
from abc import ABC, abstractmethod
# Añadimos la biblioteca matemática estándar para operaciones numéricas
import math

# Definimos la clase base abstracta Figura
class Figura(ABC):
    # Declaramos que calcular el área será un requisito obligatorio
    @abstractmethod
    def area(self) -> float:
        pass  # Sin lógica en esta sección

    # Declaramos que implementar la simulación de dibujo será obligatorio
    @abstractmethod
    def dibujar(self):
        pass  # Sin lógica en esta sección

# Subclase especializada en el comportamiento del Círculo
class Circulo(Figura):
    # Método constructor para almacenar la longitud del radio
    def __init__(self, radio: float):
        self.radio = radio  # Asignamos el valor al atributo interno

    # Calculamos la superficie empleando el valor exacto de pi
    def area(self) -> float:
        return math.pi * self.radio ** 2

    # Imprimimos la notificación que representa visualmente al círculo
    def dibujar(self):
        print(f"Dibujando un círculo de radio {self.radio}")

# Subclase especializada en el comportamiento del Rectángulo
class Rectangulo(Figura):
    # Método constructor para configurar la anchura y altura
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho  # Propiedad para almacenar la base
        self.alto = alto    # Propiedad para almacenar la altura

    # Obtenemos la superficie multiplicando ancho por alto
    def area(self) -> float:
        return self.ancho * self.alto

    # Imprimimos la notificación que representa visualmente al rectángulo
    def dibujar(self):
        print(f"Dibujando un rectángulo {self.ancho} x {self.alto}")

# Subclase especializada en el comportamiento del Triángulo
class Triangulo(Figura):
    # Método constructor para configurar la base y altura correspondientes
    def __init__(self, base: float, altura: float):
        self.base = base        # Propiedad para almacenar la base
        self.altura = altura    # Propiedad para almacenar la altura

    # Obtenemos el área siguiendo el estándar matemático habitual
    def area(self) -> float:
        return (self.base * self.altura) / 2

    # Imprimimos la notificación que representa visualmente al triángulo
    def dibujar(self):
        print(f"Dibujando un triángulo de base {self.base} y altura {self.altura}")

# Función que gestiona la llamada genérica aplicando polimorfismo
def procesar_figura(figura: Figura):
    # Llamamos a los métodos definidos en la interfaz común
    figura.dibujar()
    # Mostramos por pantalla el área formateada a un par de decimales
    print(f"Área = {figura.area():.2f}")

# Módulo de control de arranque principal
if __name__ == "__main__":
    # Creamos la colección ordenada con los datos propuestos por el profesor
    figuras = [
        Circulo(3),
        Rectangulo(4, 5),
        Triangulo(6, 2)
    ]
    
    # Recorremos de manera automatizada cada elemento dentro del arreglo
    for f in figuras:
        procesar_figura(f)  # Ejecución polimórfica individual
        print("-" * 20)      # Línea de separación para organizar la salida