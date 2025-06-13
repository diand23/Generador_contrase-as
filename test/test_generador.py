"""
Pruebas unitarias para el generador de contraseñas.
"""
import unittest
import string
from Generador_contrasenas.contrasenas import EstrategiaBasica, EstrategiaSegura, GeneradorContrasenas

class TestEstrategiaBasica(unittest.TestCase):
    """Pruebas para la Estrategia Básica."""

    def setUp(self):
        self.estrategia = EstrategiaBasica()

    def test_longitud(self):
        """Verifica que la contraseña generada tenga la longitud correcta."""
        longitud = 12
        contrasena = self.estrategia.generar(longitud)
        self.assertEqual(len(contrasena), longitud)

    def test_caracteres_validos(self):
        """Verifica que la contraseña contenga solo letras y dígitos."""
        contrasena = self.estrategia.generar(20)
        validos = string.ascii_letters + string.digits
        for c in contrasena:
            self.assertIn(c, validos)

class TestEstrategiaSegura(unittest.TestCase):
    """Pruebas para la Estrategia Segura (con símbolos)."""

    def setUp(self):
        self.estrategia = EstrategiaSegura()
        self.simbolos = "!@#$%^&*()-_=+[]{}|;:,.<>?"

    def test_longitud(self):
        """Verifica que la contraseña generada tenga la longitud correcta."""
        longitud = 15
        contrasena = self.estrategia.generar(longitud)
        self.assertEqual(len(contrasena), longitud)

    def test_contiene_simbolos(self):
        """Verifica que la contraseña contenga al menos un símbolo."""
        contrasena = self.estrategia.generar(100)  # Longitud grande para asegurar símbolos
        self.assertTrue(any(c in self.simbolos for c in contrasena))

class TestGeneradorContrasenas(unittest.TestCase):
    """Pruebas para la clase GeneradorContrasenas."""

    def test_generar_con_estrategia_basica(self):
        generador = GeneradorContrasenas(EstrategiaBasica(), longitud=8)
        contrasena = generador.generar()
        self.assertEqual(len(contrasena), 8)
        validos = string.ascii_letters + string.digits
        for c in contrasena:
            self.assertIn(c, validos)

    def test_generar_con_estrategia_segura(self):
        generador = GeneradorContrasenas(EstrategiaSegura(), longitud=20)
        contrasena = generador.generar()
        self.assertEqual(len(contrasena), 20)
        simbolos = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        self.assertTrue(any(c in simbolos for c in contrasena))

if __name__ == '__main__':
    unittest.main()

