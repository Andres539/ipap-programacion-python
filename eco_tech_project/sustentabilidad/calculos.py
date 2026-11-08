import unittest

def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    """
    Calcula las emisiones de carbono en base al consumo en kWh.
    Eleva ValueError si el consumo es negativo.
    """
    if consumo_kwh < 0:
        raise ValueError("El consumo en kWh no puede ser un valor negativo.")
    
    return consumo_kwh * factor_emision


class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_valores_nominales(self):
        """Valida la exactitud matemática con valores normales."""
        self.assertEqual(calcular_emisiones_carbono(100), 40.0)
        self.assertEqual(calcular_emisiones_carbono(250, factor_emision=0.4), 100.0)
        self.assertEqual(calcular_emisiones_carbono(0), 0.0)

    def test_consumo_negativo_eleva_value_error(self):
        """Valida que un consumo negativo lance la excepción ValueError."""
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10)


if __name__ == "__main__":
    unittest.main()