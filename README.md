# Финансовый проект

## Новый функционал

Добавлена поддержка чтения транзакций из:
- CSV файлов (функция `read_csv_file()`)
- Excel файлов (функция `read_excel_file()`)

### Использование

```python
from file_reader import read_csv_file, read_excel_file

# Чтение из CSV
transactions_csv = read_csv_file('transactions.csv')

# Чтение из Excel
transactions_excel = read_excel_file('transactions.xlsx')
```

### Зависимости

Для работы требуется:
- pandas
- openpyxl

### Критерии оценки

1. Реализованы функции для чтения:
   - CSV файлов (read_csv_file())
   - Excel файлов (read_excel_file())

2. Написаны тесты с использованием Mock

3. Поддержана типизация кода (mypy)

4. Соблюдены требования PEP 8
