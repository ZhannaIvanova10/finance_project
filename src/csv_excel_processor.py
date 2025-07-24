from typing import List, Dict, Any
import csv
import pandas as pd


def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """Считывает финансовые операции из CSV-файла.

    Args:
        file_path: Путь к CSV-файлу

    Returns:
        Список транзакций в виде словарей

    Raises:
        FileNotFoundError: Если файл не существует
        csv.Error: При ошибках чтения CSV
    """
    try:
        transactions = []
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(dict(row))
        return transactions
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Файл не найден: {file_path}") from e
    except csv.Error as e:
        raise csv.Error(f"Ошибка чтения CSV: {str(e)}") from e


def read_excel_file(file_path: str) -> List[Dict[str, Any]]:
    """Считывает финансовые операции из Excel-файла.

    Args:
        file_path: Путь к Excel-файлу

    Returns:
        Список транзакций в виде словарей

    Raises:
        ValueError: При ошибках чтения файла
        FileNotFoundError: Если файл не существует
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        # Явное преобразование ключей в строки
        return [{str(k): v for k, v in row.items()}
                for row in df.to_dict('records')]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Файл не найден: {file_path}") from e
    except Exception as e:
        raise ValueError(f"Ошибка чтения Excel файла: {str(e)}") from e
