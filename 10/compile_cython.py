# compile_cython.py - простой скрипт для компиляции
import subprocess
import sys
import os


def compile_cython():
    """Компилирует Cython файл"""
    try:
        # Проверяем, есть ли файл
        if not os.path.exists("integration_cython.pyx"):
            print("Файл integration_cython.pyx не найден!")
            return False

        print(" Компилируем Cython файл...")

        # Компилируем
        result = subprocess.run(
            [sys.executable, "setup.py", "build_ext", "--inplace"],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )

        if result.returncode == 0:
            print(" Компиляция успешна!")
            return True
        else:
            print(" Ошибка компиляции:")
            print(result.stderr)
            return False

    except Exception as e:
        print(f" Ошибка: {e}")
        return False


if __name__ == "__main__":
    compile_cython()