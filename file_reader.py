from pathlib import Path
from typing import Optional

import pandas as pd


def read_csv_file(file_path: Path | str) -> Optional[pd.DataFrame]:
    """Read CSV file and return DataFrame"""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None


def read_excel_file(file_path: Path | str) -> Optional[pd.DataFrame]:
    """Read Excel file and return DataFrame"""
    try:
        return pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None


def read_csv_file(file_path: Path | str) -> Optional[List[dict]]:
    try:
        df = pd.read_csv(file_path)
        return df.to_dict('records')  # Преобразует DataFrame в список словарей
    except Exception as e:
        print(f"Error: {e}")
        return None
