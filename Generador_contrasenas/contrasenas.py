# Crear una librería que me genere una contraseña aleatoria de longitud 8

# generador_contrasenas.py
# Librería para generar contraseñas aleatorias

import random
import string

def generar_contrasena(longitud=12, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True):
    """
    Genera una contraseña aleatoria.
    
    Parámetros:
    - longitud (int): Longitud de la contraseña.
    - usar_mayusculas (bool): Incluir letras mayúsculas.
    - usar_numeros (bool): Incluir números.
    - usar_simbolos (bool): Incluir símbolos especiales.
    
    Retorna:
    - str: Contraseña generada.
    """
    caracteres = list(string.ascii_lowercase)

    if usar_mayusculas:
        caracteres += list(string.ascii_uppercase)
    if usar_numeros:
        caracteres += list(string.digits)
    if usar_simbolos:
        caracteres += list("!@#$%^&*()-_=+[]{}|;:,.<>?")

    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de carácter.")

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena


def main():
    """
    Función principal para ejecutar el script directamente.
    Genera una contraseña y la imprime.
    """
    contrasena = generar_contrasena()
    print("Contraseña generada:", contrasena)


# Este bloque permite que el script se pueda ejecutar directamente desde consola
if __name__ == "__main__":
    main()
