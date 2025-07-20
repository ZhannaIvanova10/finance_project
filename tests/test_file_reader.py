from unittest.mock import mock_open, patch
import pytest
from src.utils.file_reader import read_json_file

def test_read_valid_json():
    json_data = '[{"amount": 100}]'
    with patch('builtins.open', mock_open(read_data=json_data)):
        assert read_json_file("test.json") == [{"amount": 100}]

def test_read_empty_file():
    with patch('builtins.open', mock_open(read_data='')):
        assert read_json_file("empty.json") == []

def test_invalid_json():
    with patch('builtins.open', mock_open(read_data='invalid')):
        assert read_json_file("bad.json") == []

def test_non_list_json():
    with patch('builtins.open', mock_open(read_data='{"key": "value"}')):
        assert read_json_file("not_list.json") == []
