def left_branch(root):
    return (root - 8) * 3
"""Вычисляет значение левого дочернего узла."""

def right_branch(root):
    return (root + 8) * 2
"""Вычисляет значение правого дочернего узла."""

def gen_bin_tree(height: int, root: int, l_b=left_branch, r_b=right_branch):
    """Генерирует бинарное дерево в виде  словаря рекурсивно. Рекурсивно строит бинарное дерево, где каждый узел представлен в виде словаря.
    Для каждого узла вычисляются левый и правый потомки с помощью функций l_b и r_b,
    после чего рекурсивно строятся поддеревья для каждого потомка."""

    d = {}
    if height > 0:
        l_branch, r_branch = l_b(root), r_b(root)
        d[root] = [gen_bin_tree(height - 1, l_branch, l_b=left_branch, r_b=right_branch),
                   gen_bin_tree(height - 1, r_branch, l_b=left_branch, r_b=right_branch)]
        return d
    else:
        d[root] = []
        return d


res = gen_bin_tree(5, 18, l_b=left_branch, r_b=right_branch)

print(res)