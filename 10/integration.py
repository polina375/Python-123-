import math
import timeit
from typing import Callable
import concurrent.futures as ftres
from functools import partial

# инерция 1
def integrate(f: Callable[[float], float], a: float, b: float, *, n_iter: int = 100000) -> float:
    """
    Вычисляет определенный интеграл функции f на интервале [a, b] методом прямоугольников.

    Arguments:
        f: Функция, интеграл которой нужно вычислить.
        a: Нижний предел интегрирования.
        b: Верхний предел интегрирования.
        n_iter: Количество прямоугольников для разбиения интервала.

    Returns:
        Приближенное значение интеграла.

    """
    if a >= b:
        raise ValueError("a must be less than b")

    acc = 0.0
    step = (b - a) / n_iter

    for i in range(n_iter):
        acc += f(a + i * step) * step

    return acc

