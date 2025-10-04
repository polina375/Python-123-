from typing import Dict, Optional


def gen_bin_tree(height: int, root: int) -> Optional[Dict]:
    """
    Рекурсивно строит бинарное дерево в виде словаря.

    Args:
        height: Высота дерева
        root: Значение корневого узла
        value: Число,которое мы передали в аргемент root

    Returns:
        Словарь, представляющий бинарное дерево, или None если высота <= 0
    """
    if height <= 0:
        return None

    left_leaf = (root - 8) * 3
    right_leaf = (root + 8) * 2

    return {
        'value': root,
        'left': gen_bin_tree(height - 1, left_leaf),
        'right': gen_bin_tree(height - 1, right_leaf)
    }

print(gen_bin_tree(18,5))