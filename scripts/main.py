# Importar librería
from Generador_contrasenas.contrasenas import generar_contrasena

# Probar la función de generación de contraseñas
generar_contrasena(longitud=16, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True)
# Imprimir la contraseña generada       
print("Contraseña generada:", generar_contrasena(longitud=16, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True))

