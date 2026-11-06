import asyncio

from matrix_spiral import get_matrix, parse_matrix, spiral_counterclockwise

SOURCE_URL = (
    "https://raw.githubusercontent.com/avito-tech/"
    "python-trainee-assignment/main/matrix.txt"
)

TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]


def test_get_matrix() -> None:
    assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL


def test_spiral_counterclockwise() -> None:
    matrix = [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
        [130, 140, 150, 160],
    ]

    assert spiral_counterclockwise(matrix) == TRAVERSAL


def test_parse_matrix() -> None:
    text = """
    +-----+-----+-----+-----+
    | 10  | 20  | 30  | 40  |
    +-----+-----+-----+-----+
    | 50  | 60  | 70  | 80  |
    +-----+-----+-----+-----+
    | 90  | 100 | 110 | 120 |
    +-----+-----+-----+-----+
    | 130 | 140 | 150 | 160 |
    +-----+-----+-----+-----+
    """

    assert parse_matrix(text) == [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
        [130, 140, 150, 160],
    ]