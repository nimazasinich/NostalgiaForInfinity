"""
این ماژول برای بررسی نحو فایل‌های پایتون استفاده می‌شود.
"""

import sys
import os
import ast


sys.setrecursionlimit(10000)  # افزایش عمق بازگشت


def check_syntax(file_path):
    """
    این تابع نحو فایل پایتون را بررسی می‌کند.

    :param file_path: مسیر فایل پایتون
    """
    try:
        with open(file_path, "r", encoding="utf-8") as source:
            ast.parse(source.read(), filename=file_path)
            print(f"Syntax check passed for {file_path}")
    except SyntaxError as e:
        print(f"Syntax error in {file_path}: {e}")
    except RecursionError as e:
        print(f"Recursion error in {file_path}: {e}")


for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            check_syntax(os.path.join(root, file))
