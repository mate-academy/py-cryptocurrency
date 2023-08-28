from typing import Callable
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked:
        yield mocked


def test_high_increase_value(mock_rate_prediction: Callable) -> None:
    mock_rate_prediction.return_value = 1530
    assert cryptocurrency_action(1000) == "Buy more cryptocurrency"


def test_minimum_increase_value(mock_rate_prediction: Callable) -> None:
    mock_rate_prediction.return_value = 1060
    assert cryptocurrency_action(1000) == "Buy more cryptocurrency"


def test_not_enough_increase_value(mock_rate_prediction: Callable) -> None:
    mock_rate_prediction.return_value = 1050
    assert cryptocurrency_action(1000) == "Do nothing"


def test_constant_value(mock_rate_prediction: Callable) -> None:
    mock_rate_prediction.return_value = 1000
    assert cryptocurrency_action(1000) == "Do nothing"


def test_with_stock_market_crash(mock_rate_prediction: Callable) -> None:
    mock_rate_prediction.return_value = 0
    assert cryptocurrency_action(1000) == "Sell all your cryptocurrency"


def test_not_enough_decrease_value(mock_rate_prediction: Callable) -> None:
    mock_rate_prediction.return_value = 950
    assert cryptocurrency_action(1000) == "Do nothing"


def test_minimum_decrease_value(mock_rate_prediction: Callable) -> None:
    mock_rate_prediction.return_value = 940
    assert cryptocurrency_action(1000) == "Sell all your cryptocurrency"


def test_high_decrease_value(mock_rate_prediction: Callable) -> None:
    mock_rate_prediction.return_value = 300
    assert cryptocurrency_action(1000) == "Sell all your cryptocurrency"


def test_raise_error_when_empty_wallet(mock_rate_prediction: Callable) -> None:
    mock_rate_prediction.return_value = 1000
    with pytest.raises(ZeroDivisionError):
        cryptocurrency_action(0)


def test_raise_error_when_wrong_type(mock_rate_prediction: Callable) -> None:
    mock_rate_prediction.return_value = "1000"
    with pytest.raises(TypeError):
        cryptocurrency_action("so much")
