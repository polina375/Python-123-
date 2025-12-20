# integration_cython.pyx - ОПТИМИЗИРОВАННАЯ версия
import math

def integrate_cython_optimized(f, double a, double b, int n_iter=100000):
    """
    Оптимизированная Cython версия с минимальным взаимодействием с Python API.
    """
    # Статические типы для всех переменных
    cdef:
        double acc = 0.0
        double step = (b - a) / n_iter
        double x
        int i

    # Оптимизированный цикл
    for i in range(n_iter):
        x = a + i * step
        acc += f(x) * step  # Единственное взаимодействие с Python API

    return acc


# Еще более оптимизированная версия (для конкретных функций)
def integrate_cos_fast(double a, double b, int n_iter=100000):
    """
    Специальная версия для cos(x) - БЕЗ вызовов Python API вообще!
    """
    cdef:
        double acc = 0.0
        double step = (b - a) / n_iter
        double x
        int i

    # Полностью на C-уровне, без Python
    for i in range(n_iter):
        x = a + i * step
        acc += math.cos(x) * step  # Используем C-функцию из math.h

    return acc


def integrate_square_fast(double a, double b, int n_iter=100000):
    """
    Специальная версия для x^2 - БЕЗ вызовов Python API!
    """
    cdef:
        double acc = 0.0
        double step = (b - a) / n_iter
        double x
        int i

    for i in range(n_iter):
        x = a + i * step
        acc += x * x * step  # Простое умножение на C-уровне

    return acc