class MatrixError(Exception):
    """Базовая ошибка библиотеки."""


class MatrixFetchError(MatrixError):
    """Ошибка получения матрицы по сети."""


class MatrixHTTPError(MatrixFetchError):
    """Сервер вернул ошибочный HTTP-статус."""

    def __init__(self, status: int, url: str) -> None:
        self.status = status
        self.url = url
        super().__init__(f"HTTP {status} при загрузке матрицы: {url}")


class MatrixParseError(MatrixError):
    """Не удалось разобрать матрицу из ответа сервера."""