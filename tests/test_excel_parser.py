from unittest.mock import patch
import pandas as pd
from src.parsers.excel_parser import read_excel_transactions


def test_read_excel_transactions():
    mock_data = pd.DataFrame({
        'id': [1, 2],
        'amount': [100, 200],
        'category': ['food', 'transport']
    })

    with patch('pandas.read_excel', return_value=mock_data):
        result = read_excel_transactions('dummy.xlsx')
        assert result == [
            {'id': 1, 'amount': 100, 'category': 'food'},
            {'id': 2, 'amount': 200, 'category': 'transport'}
        ]
