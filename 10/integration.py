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

# инерция 2
def integrate_threads(f: Callable[[float], float], a: float, b: float, *,
                      n_jobs: int = 2, n_iter: int = 1000) -> float:
    """
    Вычисляет интеграл с использованием потоков.
    """
    executor = ftres.ThreadPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, integrate, f, n_iter=n_iter // n_jobs)

    step = (b - a) / n_jobs
    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]

    return sum(f.result() for f in ftres.as_completed(fs))

# инерция 3
def integrate_processes(f: Callable[[float], float], a: float, b: float, *,
                        n_jobs: int = 2, n_iter: int = 1000) -> float:
    """
    Вычисляет интеграл с использованием процессов.
    """
    executor = ftres.ProcessPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, integrate, f, n_iter=n_iter // n_jobs)

    step = (b - a) / n_jobs
    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]

    return sum(f.result() for f in ftres.as_completed(fs))

# инерция 4
def measure_all_performance():
    """Сравнение всех методов"""
    print("СРАВНЕНИЕ")

    f = math.cos
    a, b = 0, math.pi / 2
    total_iter = 1000000

    print(f"\nФункция: cos(x) от {a} до {b}")
    print(f"Итераций: {total_iter:,}\n")

    # 1. Базовый
    print("БАЗОВЫЙ ")
    time_base = timeit.timeit(
        lambda: integrate(f, a, b, n_iter=total_iter),
        number=3
    ) / 3
    print(f"Время: {time_base:.4f} сек")

    # 2. С потоками
    print("С ПОТОКАМИ:")
    for n_jobs in [2, 4, 6]:
        time_threads = timeit.timeit(
            lambda: integrate_threads(f, a, b, n_jobs=n_jobs, n_iter=total_iter),
            number=3
        ) / 3
        speedup = time_base / time_threads if time_threads > 0 else 0
        print(f" Поток: {n_jobs}, время: {time_threads:.4f} сек, ускор: {speedup:.2f}x")

    # 3. С процессами
    print(" С ПРОЦЕССАМИ:")
    for n_jobs in [2, 4, 6]:
        time_processes = timeit.timeit(
            lambda: integrate_processes(f, a, b, n_jobs=n_jobs, n_iter=total_iter),
            number=3
        ) / 3
        speedup = time_base / time_processes if time_processes > 0 else 0
        print(f" Процесс: {n_jobs}, время: {time_processes:.4f} сек, ускор: {speedup:.2f}x")

    return {
        'base': time_base,
        'threads': time_threads,
        'processes': time_processes
    }