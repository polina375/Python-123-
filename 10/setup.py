from setuptools import setup
from Cython.Build import cythonize

setup(
    name="integration_optimized",
    ext_modules=cythonize(
        [
            "integration_cython.pyx",
        ],
        annotate=True,  # Генерируем аннотации для ВСЕХ файлов
        language_level="3"
    ),
)