# Importar librerías necesarias
from Generador_contrasenas.contrasenas import GeneradorContrasenas,EstrategiaBasica,EstrategiaSegura

# Realizar operación
def main():
    generador_seguro = GeneradorContrasenas(EstrategiaSegura(), longitud=16)
    print("Contraseña segura:", generador_seguro.generar())

    generador_basico = GeneradorContrasenas(EstrategiaBasica(), longitud=10)
    print("Contraseña básica:", generador_basico.generar())

if __name__ == "__main__":
    main()


