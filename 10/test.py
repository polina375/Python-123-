import unittest
import math
from integration import integrate


class TestIntegration(unittest.TestCase):

    def test_cos_integral(self):
        """Интеграл cos(x) от 0 до pi/2 должен быть ~1"""
        result = integrate(math.cos, 0, math.pi / 2, n_iter=10000)
        self.assertAlmostEqual(result, 1.0, delta=0.001)

    def test_quadratic_integral(self):
        """Интеграл x^2 от 0 до 1 должен быть ~1/3"""
        result = integrate(lambda x: x ** 2, 0, 1, n_iter=10000)
        self.assertAlmostEqual(result, 1 / 3, delta=0.001)

    def test_granits(self):
        """Проверка на ошибку при неправильных границах"""
        with self.assertRaises(ValueError):
            integrate(math.cos, 1, 0, n_iter=1000)


if __name__ == "__main__":
    unittest.main()