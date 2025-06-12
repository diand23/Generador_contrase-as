# Generador de contraseñas aleatorias

Una librería de Python que te de como resultado contraseñas aleatorias para diferentes usuarios.

## Instalación

```bash
pip install Generador_contrasenas
```

## Características

### Parámetros
 - longitud (int): Longitud de la contraseña.
 - usar_mayusculas (bool): Incluir letras mayúsculas.
 - usar_numeros (bool): Incluir números.
 - usar_simbolos (bool): Incluir símbolos especiales.

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
from Generador_contrasenas.contrasenas import GeneradorContrasenas

# Realizar operaciones
password1 = GeneradorContrasenas(longitud=16, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True)
password2 = GeneradorContrasenas(longitud=12, usar_mayusculas=False, usar_numeros=True, usar_simbolos=True)
password3 = GeneradorContrasenas(longitud=16, usar_mayusculas=True, usar_numeros=False, usar_simbolos=True)
password4 = GeneradorContrasenas(longitud=10, usar_mayusculas=True, usar_numeros=True, usar_simbolos=False)

# Mostrar resultados
print("Password 1:", password1)
print("Password 2:", password2)
print("Password 3:", password3)
print("Password 4:", password4)
```

## Desarrollo

1. Clona este repositorio
2. Crea un entorno virtual:
   ```bash
   python -m venv generador_contrasenas_env
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias de desarrollo:
   ```bash
   pip install -r requirements.txt
   ```
4. Instala el paquete en modo desarrollo:
   ```bash
   pip install -e .
   ```
 5. Comprobamos que aparece la librería instalada:
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
