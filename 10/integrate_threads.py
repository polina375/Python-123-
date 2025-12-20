# инерция 2
import math
import concurrent.futures as futures
from integraion import integrate


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