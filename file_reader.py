import csv
from typing import List, Dict, Any
import pandas as pd


def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Чтение финансовых операций из CSV файла.

    Args:
        file_path: Путь к CSV файлу

    Returns:
        Список словарей, где каждый словарь представляет транзакцию
    """
    transactions = []

    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(dict(row))

    return transactions


def read_excel_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Чтение финансовых операций из Excel файла.

    Args:
        file_path: Путь к Excel файлу

    Returns:
        Список словарей, где каждый словарь представляет транзакцию
    """
    df = pd.read_excel(file_path)
    return df.to_dict('records')
