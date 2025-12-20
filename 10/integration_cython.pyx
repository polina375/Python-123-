from libc.math cimport cos

def integrate(double a, double b, int n_iter):
    cdef int i
    cdef double acc = 0.0
    cdef double step = (b - a) / n_iter

    for i in range(n_iter):
        acc += cos(a + i * step) * step

    return acc
