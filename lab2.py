def guess_number (x,left, right):
    """Найти число в интервале методом линейного перебора.

    Args:
        x (int): Загаданное число для поиска
        left (int): Нижняя граница интервала (включительно)
        right (int): Верхняя граница интервала (включительно)

    Returns:
        tuple: Кортеж (result-найденное число или None, atts количество попыток)

    Example:
        >>> guess_number(5, 1, 10)
        (5, 5)
        >>> guess_number(15, 1, 10)
        (None, 10)
        """
    atts=0
    for numb in range(left,right):
        atts+=1
        if numb==x:
            return numb,atts
    return None, atts


def binary_guess_number(x,left,right):
    """
        Найти число в интервале методом бинарного поиска.

        Алгоритм  на каждом шаге уменьшая область поиска в два раза. Начинает с середины интервала
        и перемещает границы в зависимости от сравнения.

        Args:
            x (int): Загаданное число для поиска
            left (int): Нижняя граница интервала (включительно)
            right (int): Верхняя граница интервала (включительно)

        Returns:
        tuple: Кортеж (result-найденное число или None,atts-количество попыток)

        Raises:
            TypeError: Если аргументы не целые числа
            ValueError: Если left > right (неверный интервал)

        Example:
            >>> binary_guess_number(50, 1, 100)
            (50, 6)
            >>> binary_guess_number(1000, 1, 100)
            (None, 7)

        """
    atts = 0
    while left<=right:
        atts+=1
        mid = (left+right)//2
        if mid == x:
            return mid,atts
        elif mid<x:
            left=mid+1
        else:
            right=mid-1
    return None,atts
