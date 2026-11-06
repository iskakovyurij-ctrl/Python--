matrix-spiral/
├── matrix_spiral/
│   ├── __init__.py
│   ├── client.py
│   ├── exceptions.py
│   ├── parser.py
│   └── traversal.py
├── tests/
│   └── test_matrix.py
├── pyproject.toml
└── README.md
# Matrix Spiral

Библиотека асинхронно загружает квадратную матрицу по URL и возвращает
результат обхода по спирали против часовой стрелки, начиная с левого
верхнего угла.

## Установка

```bash
pip install -e .
```

## Использование

```python
import asyncio

from matrix_spiral import get_matrix

URL = (
    "https://raw.githubusercontent.com/avito-tech/"
    "python-trainee-assignment/main/matrix.txt"
)

result = asyncio.run(get_matrix(URL))
print(result)
```

## Тесты

```bash
pip install -e ".[test]"
pytest -q
```