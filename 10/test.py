import unittest
import math
from integration import integrate


class TestIntegration(unittest.TestCase):

    def test_cos_integral(self):
        """Интеграл cos(x) от 0 до pi/2 должен быть ~1"""
        result = integrate(math.cos, 0, math.pi / 2, n_iter=10000)
        self.assertAlmostEqual(result, 1.0, places=3)

    def test_iteration_stability(self):
        # результат не должен сильно меняться при увеличении n_iter
        r1 = integrate(lambda x: x ** 2, 0, 1, n_iter=1_000)
        r2 = integrate(lambda x: x ** 2, 0, 1, n_iter=10_000)
        self.assertAlmostEqual(r1, r2, places=3)

    def test_granits(self):
        """Проверка на ошибку при неправильных границах"""
        with self.assertRaises(ValueError):
            integrate(math.cos, 1, 0, n_iter=1000)


if __name__ == "__main__":
    unittest.main()