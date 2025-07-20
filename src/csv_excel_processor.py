import csv
from typing import Any, Dict, List

import pandas as pd


def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из CSV-файла.

    Args:
        file_path: Путь к CSV-файлу

    Returns:
        Список транзакций в виде словарей
    """
    transactions = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(dict(row))
    return transactions


def read_excel_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из Excel-файла.

    Args:
        file_path: Путь к Excel-файлу

    Returns:
        Список транзакций в виде словарей
    """
    df = pd.read_excel(file_path, engine='openpyxl')
    return df.to_dict('records')
