import asyncio
from typing import List

import aiohttp

from .exceptions import MatrixFetchError, MatrixHTTPError
from .parser import parse_matrix
from .traversal import spiral_counterclockwise


async def get_matrix(url: str) -> List[int]:
    """
    Асинхронно загружает квадратную матрицу по URL и возвращает
    результат обхода по спирали против часовой стрелки.

    :param url: URL текстового представления матрицы.
    :return: список чисел в порядке спирального обхода.
    :raises MatrixHTTPError: если сервер вернул HTTP-ошибку.
    :raises MatrixFetchError: при сетевой ошибке или таймауте.
    :raises MatrixParseError: если ответ не удалось разобрать как матрицу.
    """
    timeout = aiohttp.ClientTimeout(total=30, connect=10)

    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as response:
                if response.status >= 400:
                    raise MatrixHTTPError(response.status, url)

                text = await response.text()

    except asyncio.TimeoutError as exc:
        raise MatrixFetchError(f"Таймаут при загрузке матрицы: {url}") from exc
    except aiohttp.ClientError as exc:
        raise MatrixFetchError(
            f"Сетевая ошибка при загрузке матрицы {url}: {exc}"
        ) from exc

    matrix = parse_matrix(text)
    return spiral_counterclockwise(matrix)