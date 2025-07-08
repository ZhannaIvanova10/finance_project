import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from file_reader import read_csv_file, read_excel_file


class TestFileReader(unittest.TestCase):
    @patch('builtins.open',
           mock_open(read_data='id,amount,date\n1,100,2023-01-01\n2,200,2023-01-02'))
    @patch('csv.DictReader')
    def test_read_csv_file(self, mock_dict_reader):
        # Настраиваем mock
        mock_dict_reader.return_value = [
            {'id': '1', 'amount': '100', 'date': '2023-01-01'},
            {'id': '2', 'amount': '200', 'date': '2023-01-02'}
        ]

        # Тестируем
        result = read_csv_file('dummy_path.csv')

        # Проверяем
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['id'], '1')
        self.assertEqual(result[1]['amount'], '200')

    @patch('pandas.read_excel')
    def test_read_excel_file(self, mock_read_excel):
        # Настраиваем mock
        mock_data = pd.DataFrame({
            'id': [1, 2],
            'amount': [100, 200],
            'date': ['2023-01-01', '2023-01-02']
        })
        mock_read_excel.return_value = mock_data

        # Тестируем
        result = read_excel_file('dummy_path.xlsx')

        # Проверяем
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['id'], 1)
        self.assertEqual(result[1]['amount'], 200)


if __name__ == '__main__':
    unittest.main()
