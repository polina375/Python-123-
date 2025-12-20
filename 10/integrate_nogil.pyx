from libc.math cimport cos
from concurrent.futures import ThreadPoolExecutor

cdef double integrate_chunk(double a, double b, int n_iter) nogil:
    cdef int i
    cdef double acc = 0.0
    cdef double step = (b - a) / n_iter
    for i in range(n_iter):
        acc += cos(a + i * step) * step
    return acc

def integrate_threads_nogil(double a, double b, int n_iter, int n_jobs):
    step = (b - a) / n_jobs
    iters = n_iter // n_jobs

    with ThreadPoolExecutor(max_workers=n_jobs) as ex:
        futures = [
            ex.submit(
                integrate_chunk,
                a + i * step,
                a + (i + 1) * step,
                iters
            )
            for i in range(n_jobs)
        ]

        return sum(f.result() for f in futures)
