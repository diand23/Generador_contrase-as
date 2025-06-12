# Importar librería
from Generador_contrasenas.contrasenas import GeneradorContrasenas

# Probar la función de generación de contraseñas
password = GeneradorContrasenas(longitud=16, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True)
# Imprimir la contraseña generada       
print("Contraseña generada:", password)

