# 2) Figuras geométricas (área)

# Traemos las herramientas del sistema para el manejo de clases abstractas
from abc import ABC, abstractmethod
# Cargamos la librería matemática para obtener el valor exacto de Pi
import math

# Definición de la clase principal o clase padre llamada Figura
class Figura(ABC):
    
    # Declaración de la regla obligatoria para obtener el área de cada objeto
    @abstractmethod
    def area(self) -> float:
        pass  # Estructura base sin código interno

    # Declaración de la regla obligatoria para simular el dibujo en pantalla
    @abstractmethod
    def dibujar(self):
        pass  # Estructura base sin código interno

# Clase para el manejo de los círculos que hereda de Figura
class Circulo(Figura):
    # Constructor que recibe y almacena el valor del radio
    def __init__(self, radio: float):
        self.radio = radio  

    # Aplicación de la fórmula matemática para el área del círculo
    def area(self) -> float:
        return math.pi * self.radio ** 2
        
    # Mensaje informativo que simula el trazo del círculo
    def dibujar(self):
        print(f"Dibujando un círculo de radio {self.radio}")

# Clase para el manejo de los rectángulos que hereda de Figura
class Rectangulo(Figura):
    # Constructor que recibe y almacena los lados (ancho y alto)
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto
        
    # Cálculo matemático para el área del rectángulo (base por altura)
    def area(self) -> float:
        return self.ancho * self.alto
        
    # Mensaje informativo que simula el trazo del rectángulo
    def dibujar(self):
        print(f"Dibujando un rectángulo {self.ancho} x {self.alto}")

# Clase para el manejo de los triángulos que hereda de Figura
class Triangulo(Figura):
    # Constructor que recibe y almacena la base junto con la altura
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
        
    # Operación matemática para el área del triángulo (base por altura entre dos)
    def area(self) -> float:
        return (self.base * self.altura) / 2
        
    # Mensaje informativo que simula el trazo del triángulo
    def dibujar(self):
        print(f"Dibujando un triángulo de base {self.base} y altura {self.altura}")

# Función externa que aplica el polimorfismo recibiendo cualquier tipo de figura
def procesar_figura(figura: Figura):
    # Ejecuta el método dibujar correspondiente al objeto actual
    figura.dibujar()
    # Imprime en la terminal el resultado del área con un formato de dos decimales
    print(f"Área = {figura.area():.2f}")

# Estructura principal de arranque de nuestra aplicación de Python
if __name__ == "__main__":
    # Declaración de la lista que contiene los objetos con las medidas exactas del profe
    figuras = [
        Circulo(3),
        Rectangulo(4, 5),
        Triangulo(6, 2)
    ]
    
    # Ciclo iterativo para procesar cada una de las figuras de forma secuencial
    for f in figuras:
        procesar_figura(f)
        # Imprime una línea divisoria estética entre cada resultado
        print("-" * 20)