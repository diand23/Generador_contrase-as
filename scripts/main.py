import sys
import os

# Añadir la ruta a la carpeta "Generador_contrasenas"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Generador_contrasenas')))

from contrasenas import generar_contrasena
passwo = generar_contrasena(longitud=16, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True)
