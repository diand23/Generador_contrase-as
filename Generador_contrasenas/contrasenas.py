# Crear una librería que me genere una contraseña aleatoria de longitud 8

import random
import string

def generar_contrasena(longitud=12, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = list(string.ascii_lowercase)

    if usar_mayusculas:
        caracteres += list(string.ascii_uppercase)
    if usar_numeros:
        caracteres += list(string.digits)
    if usar_simbolos:
        caracteres += list("!@#$%^&*()-_=+[]{}|;:,.<>?")

    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de carácter.")

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña
