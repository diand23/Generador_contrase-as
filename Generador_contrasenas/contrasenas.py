""" Importar librerías necesarias """
import random
import string

class GeneradorContrasenas:
    def __init__(self, longitud=12, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True):
        """
         Parámetros
        - longitud (int): Longitud de la contraseña.
        - usar_mayusculas (bool): Incluir letras mayúsculas.
        - usar_numeros (bool): Incluir números.
        - usar_simbolos (bool): Incluir símbolos especiales.
        """
        self.longitud = longitud
        self.usar_mayusculas = usar_mayusculas
        self.usar_numeros = usar_numeros
        self.usar_simbolos = usar_simbolos

    def generar(self):
        """
        Genera una contraseña aleatoria basada en los parámetros del objeto.
        
        Retorna:
        - str: Contraseña generada.
        """
        caracteres = list(string.ascii_lowercase)

        if self.usar_mayusculas:
            caracteres += list(string.ascii_uppercase)
        if self.usar_numeros:
            caracteres += list(string.digits)
        if self.usar_simbolos:
            caracteres += list("!@#$%^&*()-_=+[]{}|;:,.<>?")

        if not caracteres:
            raise ValueError("Debe seleccionar al menos un tipo de carácter.")

        contrasena = ''.join(random.choice(caracteres) for _ in range(self.longitud))
        return contrasena


def generar_contrasena(longitud=12, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True):
    generador = GeneradorContrasenas(longitud, usar_mayusculas, usar_numeros, usar_simbolos)
    return generador.generar()


def main():
    """
    Ejecuta una demostración simple al correr el script directamente.
    """
    generador = GeneradorContrasenas()
    contrasena = generador.generar()
    print("Contraseña generada:", contrasena)


if __name__ == "__main__":
    main()
