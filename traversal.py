from typing import List


def spiral_counterclockwise(matrix: List[List[int]]) -> List[int]:
    """
    Обход квадратной матрицы по спирали против часовой стрелки,
    начиная с левого верхнего угла.

    Для матрицы:
        10  20  30  40
        50  60  70  80
        90 100 110 120
       130 140 150 160

    Результат:
        10, 50, 90, 130, 140, 150, 160, 120,
        80, 40, 30, 20, 60, 100, 110, 70
    """
    if not matrix:
        return []

    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("Матрица должна быть квадратной")

    result: List[int] = []

    top = 0
    bottom = size - 1
    left = 0
    right = size - 1

    while top <= bottom and left <= right:
        # Вниз по левому столбцу
        for row in range(top, bottom + 1):
            result.append(matrix[row][left])
        left += 1

        # Вправо по нижней строке
        for col in range(left, right + 1):
            result.append(matrix[bottom][col])
        bottom -= 1

        # Вверх по правому столбцу
        if top <= bottom:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][right])
            right -= 1

        # Влево по верхней строке
        if left <= right:
            for col in range(right, left - 1, -1):
                result.append(matrix[top][col])
            top += 1

    return result