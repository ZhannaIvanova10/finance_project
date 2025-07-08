import os
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

from file_reader import read_csv_file, read_excel_file


class TestFileReader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_data_dir = Path(__file__).parent / "test_data"
        cls.csv_path = cls.test_data_dir / "test.csv"
        cls.excel_path = cls.test_data_dir / "test.xlsx"

        # Создаем тестовые данные
        cls.test_csv_data = pd.DataFrame({"id": [1, 2], "amount": [100, 200]})
        cls.test_excel_data = pd.DataFrame({"id": [3, 4], "amount": [300, 400]})

    def test_read_csv_file_success(self):
        with patch("pandas.read_csv", return_value=self.test_csv_data) as mock_read:
            result = read_csv_file(self.csv_path)
            mock_read.assert_called_once_with(self.csv_path)
            pd.testing.assert_frame_equal(result, self.test_csv_data)

    def test_read_excel_file_success(self):
        with patch("pandas.read_excel", return_value=self.test_excel_data) as mock_read:
            result = read_excel_file(self.excel_path)
            mock_read.assert_called_once_with(self.excel_path)
            pd.testing.assert_frame_equal(result, self.test_excel_data)

    def test_read_csv_file_not_found(self):
        with patch("pandas.read_csv", side_effect=FileNotFoundError("File not found")):
            result = read_csv_file("nonexistent.csv")
            self.assertIsNone(result)

    def test_read_excel_file_not_found(self):
        with patch(
            "pandas.read_excel", side_effect=FileNotFoundError("File not found")
        ):
            result = read_excel_file("nonexistent.xlsx")
            self.assertIsNone(result)

    def test_read_csv_file_other_error(self):
        with patch("pandas.read_csv", side_effect=Exception("Test error")):
            result = read_csv_file("invalid.csv")
            self.assertIsNone(result)

    def test_read_excel_file_other_error(self):
        with patch("pandas.read_excel", side_effect=Exception("Test error")):
            result = read_excel_file("invalid.xlsx")
            self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
