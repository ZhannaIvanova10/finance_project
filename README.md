
# Финансовый проект

## Описание проекта
Библиотека для работы с финансовыми транзакциями. Поддерживает чтение данных из:
- JSON
- CSV (функция `read_csv_file()`)
- Excel (функция `read_excel_file()`)

## Установка

```bash
# Установка зависимостей
pip install -r requirements.txt

# Или через poetry
poetry install
```

## Использование

```python
from file_reader import read_csv_file, read_excel_file

# Чтение CSV файла
transactions = read_csv_file('data/transactions.csv')

# Чтение Excel файла
transactions = read_excel_file('data/transactions.xlsx')
```

## Тестирование

```bash
# Запуск тестов с покрытием
pytest --cov=file_reader --cov-report=term-missing

# Проверка стиля кода
flake8 file_reader.py
```

## Обработка ошибок

Функции возвращают пустой список `[]` в следующих случаях:
- Файл не существует или недоступен
- Файл пуст или не содержит данных
- Неправильный формат файла
- Ошибки парсинга данных
- Любые другие ошибки чтения

Все ошибки логируются в стандартный вывод.

## Лицензия

MIT

Последнее обновление: 09.07.2025
