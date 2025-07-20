import logging
from typing import List, Dict, Any
import json
import requests
from datetime import datetime
from src.csv_excel_processor import read_csv_file, read_excel_file


def setup_logging():
    """Настройка логирования."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('transactions.log'),
            logging.StreamHandler()
        ]
    )


def load_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает транзакции из JSON файла.

    Args:
        file_path: Путь к JSON файлу

    Returns:
        Список транзакций

    Raises:
        ValueError: При ошибках чтения JSON
    """
    try:
        with open(file_path) as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка декодирования JSON: {str(e)}")
    except Exception as e:
        raise ValueError(f"Ошибка чтения файла: {str(e)}")


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает транзакции из файла (поддерживает JSON, CSV, XLSX).

    Args:
        file_path: Путь к файлу с транзакциями

    Returns:
        Список транзакций

    Raises:
        ValueError: При неподдерживаемом формате файла
    """
    if file_path.endswith('.json'):
        return load_json_file(file_path)
    elif file_path.endswith('.csv'):
        return read_csv_file(file_path)
    elif file_path.endswith('.xlsx'):
        return read_excel_file(file_path)
    else:
        raise ValueError(f"Неподдерживаемый формат файла: {file_path}")


def get_exchange_rate(currency: str) -> float:
    """
    Получает текущий курс валюты через API.

    Args:
        currency: Код валюты (например, 'USD')

    Returns:
        Курс валюты к рублю

    Raises:
        Exception: При ошибке запроса
    """
    try:
        response = requests.get(
            f"https://api.exchangerate-api.com/v4/latest/{currency}",
            timeout=5
        )
        response.raise_for_status()
        return response.json()['rates']['RUB']
    except requests.RequestException as e:
        raise Exception(f"Ошибка получения курса валют: {str(e)}")


def process_transactions(transactions: List[Dict[str, Any]]) -> None:
    """
    Обрабатывает список транзакций.

    Args:
        transactions: Список транзакций
    """
    logger = logging.getLogger(__name__)
    total = 0

    for transaction in transactions:
        try:
            amount = float(transaction.get('amount', 0))
            currency = transaction.get('currency', 'RUB')

            if currency != 'RUB':
                rate = get_exchange_rate(currency)
                amount *= rate

            total += amount
            logger.info(f"Обработана транзакция: {transaction.get('description')}")

        except Exception as e:
            logger.error(f"Ошибка обработки транзакции: {str(e)}")

    logger.info(f"Общая сумма всех транзакций: {total:.2f} RUB")


if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Запуск приложения обработки транзакций")

    try:
        # Пример использования
        csv_transactions = load_transactions("transactions.csv")
        excel_transactions = load_transactions("transactions_excel.xlsx")
        json_transactions = load_transactions("transactions.json")

        logger.info(f"Загружено {len(csv_transactions)} транзакций из CSV")
        logger.info(f"Загружено {len(excel_transactions)} транзакций из Excel")
        logger.info(f"Загружено {len(json_transactions)} транзакций из JSON")

        process_transactions(csv_transactions + excel_transactions + json_transactions)

    except Exception as e:
        logger.error(f"Критическая ошибка: {str(e)}", exc_info=True)
