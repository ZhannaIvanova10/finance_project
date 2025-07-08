import csv
from typing import List, Dict

def read_csv_transactions(file_path: str) -> List[Dict]:
    """Читает транзакции из CSV-файла"""
    with open(file_path, encoding='utf-8') as f:
        return list(csv.DictReader(f))
