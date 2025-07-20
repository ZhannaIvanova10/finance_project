import os
from unittest.mock import patch, Mock
import pytest
from src.external_api.currency_converter import convert_to_rub


@pytest.fixture(autouse=True)
def set_env(monkeypatch):
    monkeypatch.setenv("EXCHANGE_RATE_API_KEY", "test_key")


def test_convert_rub():
    transaction = {"amount": "100", "currency": "RUB"}
    assert convert_to_rub(transaction) == 100.0


@patch('requests.get')
def test_convert_usd(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"rates": {"RUB": 75.5}}
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    transaction = {"amount": "100", "currency": "USD"}
    assert convert_to_rub(transaction) == 7550.0


def test_missing_api_key(monkeypatch):
    monkeypatch.delenv("EXCHANGE_RATE_API_KEY")
    with pytest.raises(ValueError):
        convert_to_rub({"amount": 100, "currency": "USD"})
