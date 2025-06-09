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
from Generador_contrasenas.contrasenas import generar_contrasena

# Realizar operaciones
password = generar_contrasena(longitud=16, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True)
# Imprimir la contraseña generada       
print("Contraseña generada:", password)

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

## Ejecutar Pruebas

```bash
python -m unittest tests/test_generador.py
```

## Buenas Prácticas Implementadas

1. **Programación Orientada a Objetos**: Uso de herencia y clases abstractas
2. **Modularidad**: Separación de responsabilidades en módulos
3. **Documentación**: Docstrings detallados para clases y métodos
4. **Tipado**: Uso de type hints para mejor mantenibilidad
5. **Pruebas**: Cobertura completa de pruebas unitarias
6. **Manejo de Errores**: Validación de entrada y manejo de excepciones
7. **Encapsulamiento**: Uso de propiedades para acceso controlado
8. **Código Limpio**: Nombres descriptivos y estructura clara

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.
