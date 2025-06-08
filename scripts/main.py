from generador_contrasenas import generar_contrasena

if __name__ == "__main__":
    password = generar_contrasena(
        longitud=16,
        usar_mayusculas=True,
        usar_numeros=True,
        usar_simbolos=True
    )
    print("Contraseña generada:", password)
