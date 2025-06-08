import sys
import os

# Añadir la carpeta raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Generador_contrasenas import generar_contrasena

if __name__ == "__main__":
    password = generar_contrasena(
        longitud=16,
        usar_mayusculas=True,
        usar_numeros=True,
        usar_simbolos=True
    )
    print("Contraseña generada:", password)

