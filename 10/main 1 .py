import math
import timeit
from integration import (
    integrate,
    integrate_threads,
    integrate_processes,
    measure_all_performance
)

# импортировать Cython версию
try:
    import integration_cython

    CYTHON_AVAILABLE = True
    print(" Cython версия доступна")
except ImportError:
    CYTHON_AVAILABLE = False
    print(" Cython версия не скомпилирована")
    # глушим
    integration_cython = None


def main():
    #  Базовый тест
    print("\nЧАСТЬ 1: Базовый тест функции")
    result = integrate(math.cos, 0, math.pi / 2, n_iter=1000)
    print(f"∫cos(x)dx от 0 до π/2 ≈ {result:.6f}")
    print(f"Погрешность: {abs(1.0 - result):.6f}")

    #  Cython тест
    if CYTHON_AVAILABLE:
        print("ЧАСТЬ 4")
        result_cy = integration_cython.integrate_cython(math.cos, 0, math.pi / 2, n_iter=1000)
        print(f"Результат Cython: {result_cy:.6f}")

        # Сравнение скорости
        print("\nСравнение скорости (n_iter=100000, 5 запусков):")

        time_normal = timeit.timeit(
            lambda: integrate(math.cos, 0, math.pi / 2, n_iter=100000),
            number=5
        ) / 5

        time_cython = timeit.timeit(
            lambda: integration_cython.integrate_cython(math.cos, 0, math.pi / 2, n_iter=100000),
            number=5
        ) / 5

        print(f"Python версия: {time_normal:.4f} сек")
        print(f"Cython версия: {time_cython:.4f} сек")
        print(f"Ускорение: {time_normal / time_cython:.2f}x")

    # Часть 3: Потоки и процессы
    print("ЧАСТЬ 2-3: Потоки и процессы")

    measure_all_performance()



if __name__ == "__main__":
    main()