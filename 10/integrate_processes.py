import math
import concurrent.futures as futures
from integration  import integrate
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