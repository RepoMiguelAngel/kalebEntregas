import unittest
from decimal import Decimal

from control_gastos import Gasto, agregar_gasto, calcular_total, convertir_monto


class TestControlGastos(unittest.TestCase):
    def test_convierte_monto_valido(self):
        self.assertEqual(convertir_monto("125.50"), Decimal("125.50"))

    def test_rechaza_monto_invalido_o_no_positivo(self):
        for valor in ("abc", "0", "-2", "NaN", "Infinity"):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    convertir_monto(valor)

    def test_agrega_gasto_y_limpia_descripcion(self):
        gastos = []
        gasto = agregar_gasto(gastos, "  Transporte  ", Decimal("30.00"))
        self.assertEqual(gasto, Gasto("Transporte", Decimal("30.00")))
        self.assertEqual(gastos, [gasto])

    def test_rechaza_descripcion_vacia(self):
        with self.assertRaises(ValueError):
            agregar_gasto([], "   ", Decimal("10"))

    def test_calcula_total_de_gastos(self):
        gastos = [
            Gasto("Comida", Decimal("120.25")),
            Gasto("Transporte", Decimal("35.75")),
        ]
        self.assertEqual(calcular_total(gastos), Decimal("156.00"))

    def test_total_de_lista_vacia_es_cero(self):
        self.assertEqual(calcular_total([]), Decimal("0"))


if __name__ == "__main__":
    unittest.main()
