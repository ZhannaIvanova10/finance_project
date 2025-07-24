file_reader.py
import json
import logging
from typing import List, TypedDict

import pandas as pd
from pandas.errors import EmptyDataError, ParserError

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Transaction(TypedDict):
    date: str
    amount: float
    description: str
    category: str


def read_json_file(file_path: str) -> List[Transaction]:
    """
    Читает JSON файл и возвращает список транзакций.

    Args:
        file_path (str): Путь к JSON файлу

    Returns:
        List[Transaction]: Список транзакций
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            if not isinstance(data, list):
                logger.error("JSON файл должен содержать список транзакций")
                return []
            return data
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}")
        return []
    except Exception as e:
        logger.error(f"Непредвиденная ошибка при чтении JSON: {e}")
        return []


def read_csv_file(file_path: str) -> List[Transaction]:
    """
    Читает CSV файл и возвращает список транзакций.

    Args:
        file_path (str): Путь к CSV файлу

    Returns:
        List[Transaction]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            logger.info(f"CSV файл {file_path} пуст")
            return []
        return df.to_dict('records')
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден")
        return []
    except EmptyDataError:
        logger.info(f"CSV файл {file_path} не содержит данных")
        return []
    except ParserError:
        logger.error(f"Ошибка парсинга CSV в файле {file_path}")
        return []
    except Exception as e:
        logger.error(f"Непредвиденная ошибка при чтении CSV: {e}")
        return []


def read_excel_file(file_path: str) -> List[Transaction]:
    """
    Читает Excel файл и возвращает список транзакций.

    Args:
        file_path (str): Путь к Excel файлу (.xlsx)

    Returns:
        List[Transaction]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        if df.empty:
            logger.info(f"Excel файл {file_path} пуст")
            return []
        return df.to_dict('records')
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден")
        return []
    except EmptyDataError:
        logger.info(f"Excel файл {file_path} не содержит данных")
        return []
    except ValueError as e:
        logger.error(f"Ошибка формата Excel файла: {e}")
        return []
    except Exception as e:
        logger.error(f"Непредвиденная ошибка при чтении Excel: {e}")
        return []
