def left_branch(root):
    """Вычисляет значение левого дочернего узла."""
    return (root - 8) * 3

def right_branch(root):
    """Вычисляет значение правого дочернего узла."""
    return (root + 8) * 2


def gen_bin_tree1(height: int, root: int, l=left_branch, r=right_branch):
    """Генерирует бинарное дерево в виде  словаря нерекурсивно
    Параметры:
        height (int): Высота дерева, количество ковней
        root (int): Начальное число, от которого происходят все вычисления по формулам"""

    if height < 0:
        return {}

    tree = {str(root): []}
    current_level = [(root, str(root))]

    for nodes in range(height):
        next_level = []
        for parent_value, key in current_level:
            left_v = l(parent_value)
            right_v = r(parent_value)

            tree[str(left_v)] = []
            tree[str(right_v)] = []
            tree[key].append({str(left_v): tree[str(left_v)]})
            tree[key].append({str(right_v): tree[str(right_v)]})

            next_level.append((left_v, str(left_v)))
            next_level.append((right_v, str(right_v)))

        current_level = next_level

    return {str(root): tree[str(root)]}