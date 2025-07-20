# Обработчик финансовых транзакций

Проект для обработки транзакций из JSON/CSV/Excel с конвертацией валют.

## Функционал
- Чтение транзакций из JSON
- Конвертация USD/EUR в RUB
- Логирование операций

## Установка
1. Скопируйте `.env.template` в `.env`
2. Установите зависимости:
```bash
pip install -r requirements.txt

## Пример использования

```python
from src.utils.file_reader import read_json_file
from src.external_api.currency_converter import convert_to_rub

transactions = read_json_file("data/operations.json")
for tx in transactions:
    amount_rub = convert_to_rub(tx)
    print(f"{tx['description']}: {amount_rub:.2f} RUB")
