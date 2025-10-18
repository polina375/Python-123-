import timeit
import matplotlib.pyplot as plt


def left_branch(root):
    return (root - 8) * 3


def right_branch(root):
    return (root + 8) * 2


def gen_bin_tree(height: int, root: int, l_b=left_branch, r_b=right_branch):
    """Генерирует бинарное дерево в виде вложенной словарной структуры."""

    d = {}
    if height > 0:
        l_branch, r_branch = l_b(root), r_b(root)
        d[root] = [gen_bin_tree(height - 1, l_branch, l_b=left_branch, r_b=right_branch),
                   gen_bin_tree(height - 1, r_branch, l_b=left_branch, r_b=right_branch)]
        return d
    else:
        d[root] = []
        return d

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

def benchmark(func, *args, repeat=5):
    """Возвращает среднее время выполнения func за repeat повторов"""
    times = timeit.repeat(lambda: func(args), number=1, repeat=repeat)
    return min(times)



def main():
    # фиксированный набор данных
    test_data = list(range(1, 24))

    res_recursive = []
    res_iterative = []

    for n in test_data:
        res_recursive.append(benchmark(gen_bin_tree, [n], 0))
        res_iterative.append(benchmark(gen_bin_tree1, [n],  0))

    # Визуализация
    plt.plot(test_data, gen_bin_tree, label="Рекурсивный")
    plt.plot(test_data, gen_bin_tree1 , label="Итеративный")
    plt.xlabel("высота дерева")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение рекурсивного и итеративного построение девера")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

