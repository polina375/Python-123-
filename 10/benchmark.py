import math, time
from integrate_threads import integrate_threads
from integrate_processes import integrate_processes
from integrate_nogil import integrate_threads_nogil

for jobs in (2, 4, 6):
    t = time.time()
    integrate_threads(math.sin, 0, math.pi, n_jobs=jobs)
    print("threads:", jobs, time.time() - t)

    t = time.time()
    integrate_processes(math.sin, 0, math.pi, n_jobs=jobs)
    print("processes:", jobs, time.time() - t)

    t = time.time()
    integrate_threads_nogil(0, math.pi, 1_000_000, jobs)
    print("nogil:", jobs, time.time() - t)
