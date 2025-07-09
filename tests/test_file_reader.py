import json
import pandas as pd
import pytest
from unittest.mock import patch, mock_open
from pandas.errors import ParserError, EmptyDataError
from file_reader import read_csv_file, read_excel_file, read_json_file, logger


@pytest.fixture
def sample_csv(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text("date,amount\n2023-01-01,100.0")
    return str(file)


@pytest.fixture
def sample_json(tmp_path):
    file = tmp_path / "test.json"
    file.write_text('[{"date": "2023-01-01", "amount": 100.0}]')
    return str(file)


# JSON Tests
def test_read_json_file_valid(sample_json):
    result = read_json_file(sample_json)
    assert len(result) == 1
    assert result[0]["date"] == "2023-01-01"


def test_read_json_file_invalid_data(tmp_path):
    file = tmp_path / "test.json"
    file.write_text('{"not_a_list": true}')
    result = read_json_file(str(file))
    assert result == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_json_file_not_found(mock_open):
    result = read_json_file("nonexistent.json")
    assert result == []


@patch("builtins.open", side_effect=Exception("Test error"))
def test_read_json_general_exception(mock_open):
    result = read_json_file("error.json")
    assert result == []


# CSV Tests
def test_read_csv_file_valid(sample_csv):
    result = read_csv_file(sample_csv)
    assert len(result) == 1
    assert result[0]["date"] == "2023-01-01"


@patch("pandas.read_csv", side_effect=Exception("Test error"))
def test_read_csv_file_general_error(mock_read):
    result = read_csv_file("test.csv")
    assert result == []


@patch("pandas.read_csv")
def test_read_csv_empty_file(mock_read):
    mock_read.return_value = pd.DataFrame()
    with patch.object(logger, 'info') as mock_log:
        result = read_csv_file("empty.csv")
        assert result == []
        mock_log.assert_called_with("CSV файл empty.csv пуст")


@patch("pandas.read_csv", side_effect=ParserError("Parse error"))
def test_read_csv_parser_error(mock_read):
    with patch.object(logger, 'error') as mock_log:
        result = read_csv_file("bad.csv")
        assert result == []
        mock_log.assert_called_with("Ошибка парсинга CSV в файле bad.csv")


@patch("pandas.read_csv", side_effect=FileNotFoundError())
def test_read_csv_file_not_found(mock_read):
    with patch.object(logger, 'error') as mock_log:
        result = read_csv_file("missing.csv")
        assert result == []
        mock_log.assert_called_with("Файл missing.csv не найден")


# Excel Tests
@patch("pandas.read_excel")
def test_read_excel_file_valid(mock_read):
    mock_read.return_value = pd.DataFrame([{"date": "2023-01-01", "amount": 100.0}])
    result = read_excel_file("test.xlsx")
    assert len(result) == 1
    assert result[0]["date"] == "2023-01-01"


@patch("pandas.read_excel", side_effect=ValueError("Test error"))
def test_read_excel_file_value_error(mock_read):
    result = read_excel_file("test.xlsx")
    assert result == []


@patch("pandas.read_excel")
def test_read_excel_empty_file(mock_read):
    mock_read.return_value = pd.DataFrame()
    with patch.object(logger, 'info') as mock_log:
        result = read_excel_file("empty.xlsx")
        assert result == []
        mock_log.assert_called_with("Excel файл empty.xlsx пуст")


@patch("pandas.read_excel", side_effect=FileNotFoundError())
def test_read_excel_file_not_found(mock_read):
    with patch.object(logger, 'error') as mock_log:
        result = read_excel_file("nonexistent.xlsx")
        assert result == []
        mock_log.assert_called_with("Файл nonexistent.xlsx не найден")


@patch("pandas.read_excel", side_effect=Exception("Test error"))
def test_read_excel_general_exception(mock_read):
    with patch.object(logger, 'error') as mock_log:
        result = read_excel_file("error.xlsx")
        assert result == []
        mock_log.assert_called_with("Непредвиденная ошибка при чтении Excel: Test error")


@patch("pandas.read_excel", side_effect=EmptyDataError())
def test_read_excel_empty_data_error(mock_read):
    with patch.object(logger, 'info') as mock_log:
        result = read_excel_file("empty_data.xlsx")
        assert result == []
        mock_log.assert_called_with("Excel файл empty_data.xlsx не содержит данных")

# Дополнительные тесты для полного покрытия
def test_read_json_decode_error(tmp_path):
    file = tmp_path / "bad.json"
    file.write_text('{"invalid": json}')
    with patch.object(logger, 'error') as mock_log:
        result = read_json_file(str(file))
        assert result == []
        mock_log.assert_called_with(f"Ошибка декодирования JSON в файле {str(file)}")

def test_read_csv_empty_data_error():
    with patch("pandas.read_csv", side_effect=EmptyDataError()):
        with patch.object(logger, 'info') as mock_log:
            result = read_csv_file("empty.csv")
            assert result == []
            mock_log.assert_called_with("CSV файл empty.csv не содержит данных")
