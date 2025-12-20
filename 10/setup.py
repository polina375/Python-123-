from setuptools import setup
from Cython.Build import cythonize

setup(
    name="integration_optimized",
    ext_modules=cythonize(
        [
            "integration_cython.pyx",
            "integration_cython_opt.pyx"
        ],
        annotate=True,  # Генерируем аннотации для ВСЕХ файлов
        language_level="3"
    ),
)