# integration_cython_opt.pyx - МАКСИМАЛЬНО оптимизированная версия
cimport cython
from libc.math cimport cos, sin

@cython.boundscheck(False)  # Отключаем проверки границ
@cython.wraparound(False)   # Отключаем отрицательные индексы
@cython.cdivision(True)     # Используем C-деление (без проверки на 0)
def integrate_cython_fast(f, double a, double b, int n_iter=100000):
    """
    Максимально оптимизированная версия.
    """
    cdef:
        double acc = 0.0
        double step = (b - a) / n_iter
        double x
        int i

    # Все переменные на уровне C, минимум взаимодействия с Python
    for i in range(n_iter):
        x = a + i * step
        acc += f(x) * step  # Это единственный вызов Python API

    return acc


# Версия БЕЗ GIL для использования с потоками
def integrate_nogil(f, double a, double b, int n_iter=100000):
    """
    Версия с отключением GIL для использования в потоках.
    """
    cdef:
        double acc = 0.0
        double step = (b - a) / n_iter
        double x
        int i

    # Отключаем GIL на время вычислений
    with nogil:
        for i in range(n_iter):
            x = a + i * step
            # ВАЖНО: f(x) вызывает Python, поэтому нужен gil
            # В реальном коде здесь должна быть C-функция
            with gil:
                acc += f(x) * step

    return acc


# Специальная версия для cos с полным отключением GIL
def integrate_cos_nogil(double a, double b, int n_iter=100000):
    """
    Интегрирование cos(x) БЕЗ GIL - может работать в потоках!
    """
    cdef:
        double acc = 0.0
        double step = (b - a) / n_iter
        double x
        int i

    # Полностью без GIL и без Python API!
    with nogil:
        for i in range(n_iter):
            x = a + i * step
            acc += cos(x) * step  # Используем C-функцию cos

    return acc