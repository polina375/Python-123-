import timeit
import matplotlib.pyplot as plt
import sys
from functools import lru_cache


sys.setrecursionlimit(2000)



def fact_recursive(n: int) -> int:
    """Рекурсивный факториал без оптимизации"""
    if n == 0:
        return 1
    return n * fact_recursive(n - 1)


def fact_iterative(n: int) -> int:
    """Нерекурсивный факториал без оптимизации"""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res



@lru_cache(maxsize=None)
def fact_recursive_memo(n: int) -> int:
    """Рекурсивный факториал с мемоизацией"""
    if n == 0:
        return 1
    return n * fact_recursive_memo(n - 1)



@lru_cache(maxsize=None)
def fact_iterative_memo(n: int) -> int:
    """Нерекурсивный факториал с 'мемоизацией' (для сравнения)"""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def benchmark(func, data, number=1000, repeat=3):
    """Возвращает среднее время выполнения func на наборе data"""
    total = 0
    for n in data:
        # Сбрасываем кэш для мемоизированных функций перед каждым тестом
        if hasattr(func, 'cache_clear'):
            func.cache_clear()
        times = timeit.repeat(lambda: func(n), number=number, repeat=repeat)
        total += min(times)
    return total / len(data)


def plot_comparison_1():
    """Первый способ сравнения: lru_cache vs без оптимизации"""
    test_data = list(range(5, 100, 5))

    # Сравнение с мемоизацией
    recursive_memo_times = []
    iterative_memo_times = []

    # Сравнение без оптимизации
    recursive_na_times = []
    iterative_na_times = []

    for n in test_data:
        # Тестируем версии с мемоизацией
        recursive_memo_times.append(benchmark(fact_recursive_memo, [n], number=10000, repeat=3))
        iterative_memo_times.append(benchmark(fact_iterative_memo, [n], number=10000, repeat=3))

        # Тестируем версии без оптимизации
        recursive_na_times.append(benchmark(fact_recursive, [n], number=10000, repeat=3))
        iterative_na_times.append(benchmark(fact_iterative, [n], number=10000, repeat=3))

    # График 1: Сравнение lru_cache РекФакт и НРекФакт
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(test_data, recursive_memo_times, label="Рекурсивный (lru_cache)", color='blue', linewidth=2)
    plt.plot(test_data, iterative_memo_times, label="Итеративный (lru_cache)", color='red', linewidth=2)
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение с мемоизацией")
    plt.legend()
    plt.grid(True)

    # График 2: Сравнение без оптимизации РекФакт и НРекФакт
    plt.subplot(1, 2, 2)
    plt.plot(test_data, recursive_na_times, label="Рекурсивный (без оптимизации)", color='blue', linewidth=2)
    plt.plot(test_data, iterative_na_times, label="Итеративный (без оптимизации)", color='red', linewidth=2)
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение без оптимизации")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def plot_comparison_2():
    """Второй способ сравнения: влияние мемоизации на каждый метод"""
    test_data = list(range(5, 100, 5))

    # Данные для рекурсивных версий
    recursive_memo_times = []
    recursive_na_times = []

    # Данные для итеративных версий
    iterative_memo_times = []
    iterative_na_times = []

    for n in test_data:
        # Рекурсивные версии
        recursive_memo_times.append(benchmark(fact_recursive_memo, [n], number=10000, repeat=3))
        recursive_na_times.append(benchmark(fact_recursive, [n], number=10000, repeat=3))

        # Итеративные версии
        iterative_memo_times.append(benchmark(fact_iterative_memo, [n], number=10000, repeat=3))
        iterative_na_times.append(benchmark(fact_iterative, [n], number=10000, repeat=3))

    # График 1: Влияние мемоизации на рекурсивную версию
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(test_data, recursive_memo_times, label="С мемоизацией", color='green', linewidth=2)
    plt.plot(test_data, recursive_na_times, label="Без оптимизации", color='orange', linewidth=2)
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Рекурсивный метод: влияние мемоизации")
    plt.legend()
    plt.grid(True)

    # График 2: Влияние мемоизации на итеративную версию
    plt.subplot(1, 2, 2)
    plt.plot(test_data, iterative_memo_times, label="С мемоизацией", color='green', linewidth=2)
    plt.plot(test_data, iterative_na_times, label="Без оптимизации", color='orange', linewidth=2)
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Итеративный метод: влияние мемоизации")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def plot_comprehensive_comparison():
    """Полное сравнение всех четырех методов"""
    test_data = list(range(5, 100, 5))

    times_recursive_na = []
    times_recursive_memo = []
    times_iterative_na = []
    times_iterative_memo = []

    for n in test_data:
        times_recursive_na.append(benchmark(fact_recursive, [n], number=10000, repeat=3))
        times_recursive_memo.append(benchmark(fact_recursive_memo, [n], number=10000, repeat=3))
        times_iterative_na.append(benchmark(fact_iterative, [n], number=10000, repeat=3))
        times_iterative_memo.append(benchmark(fact_iterative_memo, [n], number=10000, repeat=3))

    plt.figure(figsize=(12, 8))

    plt.plot(test_data, times_recursive_na, label="Рекурсивный (без оптимизации)", linewidth=2)
    plt.plot(test_data, times_recursive_memo, label="Рекурсивный (lru_cache)", linewidth=2)
    plt.plot(test_data, times_iterative_na, label="Итеративный (без оптимизации)", linewidth=2)
    plt.plot(test_data, times_iterative_memo, label="Итеративный (lru_cache)", linewidth=2)

    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Полное сравнение методов вычисления факториала")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    print("Сравнение методов вычисления факториала")
    print("=" * 50)

    # Демонстрация работы функций
    test_n = 10
    print(f"Факториал {test_n}:")
    print(f"Рекурсивный (без оптимизации): {fact_recursive(test_n)}")
    print(f"Рекурсивный (с мемоизацией): {fact_recursive_memo(test_n)}")
    print(f"Итеративный (без оптимизации): {fact_iterative(test_n)}")
    print(f"Итеративный (с мемоизацией): {fact_iterative_memo(test_n)}")

    # Запуск сравнений
    print("\n1. Сравнение lru_cache vs без оптимизации...")
    plot_comparison_1()

    print("\n2. Сравнение влияния мемоизации на каждый метод...")
    plot_comparison_2()

    print("\n3. Полное сравнение всех методов...")
    plot_comprehensive_comparison()


if __name__ == "__main__":
    main()