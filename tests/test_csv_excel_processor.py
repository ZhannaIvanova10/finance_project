from unittest.mock import patch, mock_open
import pandas as pd
import pytest
from src.csv_excel_processor import read_csv_file, read_excel_file

CSV_DATA = """id,amount,date,description
1,100,2023-01-01,Payment
2,200,2023-01-02,Transfer"""

EXCEL_DATA = [
    {"id": 1, "amount": 100, "date": "2023-01-01", "description": "Payment"},
    {"id": 2, "amount": 200, "date": "2023-01-02", "description": "Transfer"}
]


class TestCSVProcessor:
    """Тесты для работы с CSV файлами."""

    def test_read_csv_file_success(self):
        """Тест успешного чтения CSV файла."""
        with patch('builtins.open', mock_open(read_data=CSV_DATA)):
            result = read_csv_file('dummy.csv')
            assert len(result) == 2
            assert result[0]['id'] == '1'
            assert result[1]['amount'] == '200'

    def test_read_csv_file_not_found(self):
        """Тест обработки отсутствия файла."""
        with pytest.raises(FileNotFoundError):
            read_csv_file('nonexistent.csv')


class TestExcelProcessor:
    """Тесты для работы с Excel файлами."""

    @patch('pandas.read_excel')
    def test_read_excel_file_success(self, mock_read_excel):
        """Тест успешного чтения Excel файла."""
        mock_read_excel.return_value = pd.DataFrame(EXCEL_DATA)
        result = read_excel_file('dummy.xlsx')
        assert len(result) == 2
        assert result[0]['id'] == 1
        assert result[1]['description'] == 'Transfer'

    @patch('pandas.read_excel')
    def test_read_excel_file_error(self, mock_read_excel):
        """Тест обработки ошибки чтения Excel."""
        mock_read_excel.side_effect = Exception("Excel read error")
        with pytest.raises(ValueError):
            read_excel_file('error.xlsx')
