import csv
from typing import List, Dict, Any
import pandas as pd


def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает финансовые операции из CSV файла.

    Args:
        file_path: Путь к CSV файлу

    Returns:
        Список словарей с транзакциями

    Raises:
        FileNotFoundError: Если файл не найден
        csv.Error: При ошибках чтения CSV
    """
    transactions = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                transactions.append(dict(row))
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден")
    except csv.Error as e:
        raise csv.Error(f"Ошибка чтения CSV: {str(e)}")

    return transactions


def read_excel_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает финансовые операции из Excel файла.

    Args:
        file_path: Путь к Excel файлу

    Returns:
        Список словарей с транзакциями

    Raises:
        FileNotFoundError: Если файл не найден
        ValueError: При ошибках чтения Excel
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        return df.to_dict('records')
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден")
    except Exception as e:
        raise ValueError(f"Ошибка чтения Excel: {str(e)}")
