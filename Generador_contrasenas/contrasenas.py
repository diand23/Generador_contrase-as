""" Importar librerías necesarias """
import random
import string
from abc import ABC, abstractmethod

# Estrategia base
class EstrategiaContrasena(ABC):
    @abstractmethod
    def generar(self, longitud: int) -> str:
        pass

# Estrategia básica
class EstrategiaBasica(EstrategiaContrasena):
    def generar(self, longitud):
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for _ in range(longitud))

# Estrategia con símbolos
class EstrategiaSegura(EstrategiaContrasena):
    def generar(self, longitud):
        caracteres = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?"
        return ''.join(random.choice(caracteres) for _ in range(longitud))

# Contexto
class GeneradorContrasenas:
    def __init__(self, estrategia: EstrategiaContrasena, longitud=12):
        self.estrategia = estrategia
        self.longitud = longitud

    def generar(self):
        return self.estrategia.generar(self.longitud)

# Punto de entrada para la terminal
def main():
    generador = GeneradorContrasenas(EstrategiaSegura(), longitud=16)
    print("Contraseña segura:", generador.generar())

    generador = GeneradorContrasenas(EstrategiaBasica(), longitud=10)
    print("Contraseña básica:", generador.generar())

if __name__ == "__main__":
    main()