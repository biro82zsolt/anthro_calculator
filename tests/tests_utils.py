# tests/test_utils.py

import unittest
from anthro_app.utils import calculate_plx, calculate_mk, calculate_vttm


class TestAnthropometryUtils(unittest.TestCase):

    def test_calculate_plx(self):
        self.assertEqual(calculate_plx(20, 30, 10), 60)
        self.assertEqual(calculate_plx(0, 0, 0), 0)
        self.assertAlmostEqual(calculate_plx(15.5, 20.2, 4.3), 40.0, places=1)

    def test_calculate_mk(self):
        # Teszt korrekció nélkül (eltérés = 0)
        result = calculate_mk(ttm_kor=16, tts_kor=16, plx_kor=16, dck=16, diff=0)
        expected = 0.25 * (16 + 16 + 16 + 16) * 1
        self.assertAlmostEqual(result, expected)

        # Teszt pozitív korrekcióval (diff < -2)
        result = calculate_mk(15, 15, 15, 15, diff=-2.5)
        expected = 0.25 * (15 + 15 + 15 + 15) * 1.08
        self.assertAlmostEqual(result, expected)

        # Teszt negatív korrekcióval (diff > 2)
        result = calculate_mk(17, 17, 17, 17, diff=2.1)
        expected = 0.25 * (17 + 17 + 17 + 17) * 0.92
        self.assertAlmostEqual(result, expected)

    def test_calculate_vttm(self):
        # Fiú (default)
        result = calculate_vttm(height=160, dck=15, gender="m")
        self.assertAlmostEqual(result, 160 + (18 - 15) * 0.6)

        # Lány
        result = calculate_vttm(height=150, dck=14.5, gender="f")
        self.assertAlmostEqual(result, 150 + (18 - 14.5) * 0.5)


if __name__ == "__main__":
    unittest.main()
