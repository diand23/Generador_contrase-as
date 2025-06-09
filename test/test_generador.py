from Generador_contrasenas.contrasenas import generar_contrasena

# Realizar operaciones
password1 = generar_contrasena(longitud=16, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True)
password2 = generar_contrasena(longitud=12, usar_mayusculas=False, usar_numeros=True, usar_simbolos=True)
password3 = generar_contrasena(longitud=16, usar_mayusculas=True, usar_numeros=False, usar_simbolos=True)
password4 = generar_contrasena(longitud=10, usar_mayusculas=True, usar_numeros=True, usar_simbolos=False)

# Mostrar resultados
print("Password 1:", password1)
print("Password 2:", password2)
print("Password 3:", password3)
print("Password 4:", password4)
