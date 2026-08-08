import pytest
from app.main import cryptocurrency_action
from unittest.mock import patch


@pytest.fixture
def mock_exchange_rate_prediction() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock:
        yield mock


def test_cryptocurrency_action_buy(
        mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 1.06 * 100
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell(
        mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 0.94 * 100
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing(
        mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 0.98 * 100
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


def test_rate_105_percent_do_nothing(
        mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 1.05 * 100
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


def test_rate_95_percent_do_nothing(
        mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 0.95 * 100
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
