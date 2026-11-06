import re
from math import isqrt
from typing import List

from .exceptions import MatrixParseError

_NUMBER_RE = re.compile(r"\d+")


def parse_matrix(text: str) -> List[List[int]]:
    """
    Извлекает квадратную матрицу из текстового представления.

    Форматирование таблицы может меняться, поэтому числа извлекаются
    регулярным выражением, после чего проверяется, что их количество
    образует квадрат.
    """
    values = [int(match.group()) for match in _NUMBER_RE.finditer(text)]

    if not values:
        raise MatrixParseError("В ответе сервера не найдено чисел матрицы")

    size = isqrt(len(values))
    if size * size != len(values):
        raise MatrixParseError(
            f"Количество чисел не образует квадратную матрицу: {len(values)}"
        )

    return [
        values[row * size : (row + 1) * size]
        for row in range(size)
    ]