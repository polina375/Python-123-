import math
from main import logger


@logger
def solve_quadratic(a, b, c):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise TypeError("Коэффициенты должны быть числами")

    if a == 0:
        raise ValueError("Коэффициент a не может быть 0")

    D = b ** 2 - 4 * a * c

    if D < 0:
        return None
    elif D == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return x1, x2



print(solve_quadratic(1, -3, 2))
print(solve_quadratic(1, 2, 5))