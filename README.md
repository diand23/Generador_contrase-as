# Generador de contraseñas aleatorias

Una librería de Python que te de como resultado contraseñas aleatorias para diferentes usuarios.

## Instalación

```bash
pip install Generador_contrasenas
```

## Características

### Generador de contraseñas aleatorias Básica
Contraseñas aleatorias compuestas por caracteres de tipo string.

### Generador de contraseñas aleatorias Seguras
Contraseñas aleatorias compuestas por caracteres especiales, obteniendo
una mayor complejidad. 

## Estructura del Proyecto
```
Generador_contrasenas/
├── Generador_contrasenas/
│   └── __init__.py
│   ├── contrasenas.py
├── scripts/
│   └── main.py
├── test
|    └── test_generador.py
├── setup.py
├── requirements.txt
└── README.md
```

## Uso

### Generador de contraseñas
```python
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
```

## Desarrollo

1. Clona este repositorio
2. Crea un entorno virtual:
   ```bash
   python -m venv generador_contrasenas_env
   venv\Scripts\activate
   ```
3. Instala las dependencias de desarrollo:
   ```bash
   pip install -r requirements.txt
   ```
4. Instala el paquete en modo desarrollo:
   ```bash
   pip install -e .
   ```
 5. Validamos que aparece la librería instalada:
    ```bash
    pip list
    ```  

## Ejecutar Pruebas

```bash
python -m unittest test/test_generador.py
```

## Buenas Prácticas Implementadas

1. **Programación Orientada a Objetos**: Uso de herencia y clases abstractas
2. **Patrón Strategy**: aplicación de un patrón de diseño
3. **Modularidad**: Separación de responsabilidades en módulos
4. **Documentación**: Docstrings detallados para clases y métodos
5. **Tipado**: Uso de type hints para mejor mantenibilidad
6. **Pruebas**: Cobertura completa de pruebas unitarias
7. **Manejo de Errores**: Validación de entrada y manejo de excepciones
8. **Encapsulamiento**: Uso de propiedades para acceso controlado
9. **Código Limpio**: Nombres descriptivos y estructura clara

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.
