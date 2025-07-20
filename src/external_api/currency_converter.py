import logging
import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с ключами 'amount' и 'currency'

    Returns:
        Сумма в рублях (float)

    Raises:
        ValueError: Если отсутствует API ключ
        Exception: При ошибках запроса
    """
    try:
        amount = float(transaction['amount'])
        currency = transaction.get('currency', 'RUB')

        if currency == 'RUB':
            return amount

        api_key = os.getenv('EXCHANGE_RATE_API_KEY')
        if not api_key:
            raise ValueError("API ключ не найден в .env")

        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/latest?base={currency}",
            headers={"apikey": api_key},
            timeout=5
        )
        response.raise_for_status()

        return amount * response.json()['rates']['RUB']

    except requests.Timeout:
        logger.error("Таймаут при запросе курса валют")
        raise Exception("Превышено время ожидания ответа от API")
    except requests.RequestException as e:
        logger.error(f"Ошибка API: {str(e)}")
        raise Exception(f"Ошибка конвертации: {str(e)}")
