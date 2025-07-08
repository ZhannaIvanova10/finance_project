from unittest.mock import mock_open, patch
from src.parsers.csv_parser import read_csv_transactions

def test_read_csv_transactions():
    mock_data = "id,amount,category\n1,100,food\n2,200,transport"
    with patch('builtins.open', mock_open(read_data=mock_data)):
        result = read_csv_transactions('dummy.csv')
        assert result == [
            {'id': '1', 'amount': '100', 'category': 'food'},
            {'id': '2', 'amount': '200', 'category': 'transport'}
        ]
