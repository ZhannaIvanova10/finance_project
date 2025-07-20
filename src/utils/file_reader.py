import json
import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON файл с транзакциями.

    Args:
        file_path: Путь к JSON файлу

    Returns:
        Список словарей с транзакциями или пустой список при ошибках

    Examples:
        >>> read_json_file("data/operations.json")
        [{"date": "2023-01-01", "amount": 100.0, ...}]
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
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
        logger.error(f"Непредвиденная ошибка: {str(e)}")
        return []
