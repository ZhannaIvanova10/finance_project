# Финансовый проект

## Новый функционал

Добавлена поддержка чтения транзакций из:
- CSV файлов (функция `read_csv_file()`)
- Excel файлов (функция `read_excel_file()`)

### Использование

```python
from file_reader import read_csv_file, read_excel_file

# Чтение из CSV
transactions_csv = read_csv_file('data/transactions.csv')

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
<<<<<<< HEAD
\n\nLast updated: Tue Jul  8 18:56:26 RTZ 2025
=======



## Поддержка CSV и Excel

Теперь проект может читать транзакции из:
- CSV-файлов (`read_csv_transactions()`)
- Excel-файлов (`read_excel_transactions()`)
>>>>>>> b7b5cbbd8f06f6a36a816a374a500cf54eb42310
