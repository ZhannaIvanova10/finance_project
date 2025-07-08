import pandas as pd
from typing import List, Dict

def read_excel_transactions(file_path: str) -> List[Dict]:
    """Читает транзакции из Excel-файла"""
    return pd.read_excel(file_path, engine='openpyxl').to_dict('records')
