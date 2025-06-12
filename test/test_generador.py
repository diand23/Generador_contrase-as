
from Generador_contrasenas.contrasenas import EstrategiaBasica, EstrategiaSegura, GeneradorContrasenas

# Test para el generador de contraseñas
class TestGeneradorContrasenas(unittest.TestCase):

    def test_estrategia_basica_longitud(self):
        estrategia = EstrategiaBasica()
        contrasena = estrategia.generar(12)
        self.assertEqual(len(contrasena), 12)

    def test_estrategia_basica_caracteres_validos(self):
        estrategia = EstrategiaBasica()
        contrasena = estrategia.generar(20)
        for c in contrasena:
            self.assertIn(c, string.ascii_letters + string.digits)

    def test_estrategia_segura_longitud(self):
        estrategia = EstrategiaSegura()
        contrasena = estrategia.generar(15)
        self.assertEqual(len(contrasena), 15)

    def test_estrategia_segura_contiene_simbolos(self):
        estrategia = EstrategiaSegura()
        contrasena = estrategia.generar(100)
        simbolos = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        self.assertTrue(any(c in simbolos for c in contrasena))

    def test_generador_usa_estrategia_correctamente(self):
        generador = GeneradorContrasenas(EstrategiaBasica(), longitud=8)
        contrasena = generador.generar()
        self.assertEqual(len(contrasena), 8)
        self.assertTrue(all(c in string.ascii_letters + string.digits for c in contrasena))

if __name__ == '__main__':
    unittest.main()
