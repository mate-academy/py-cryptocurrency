import pytest
from unittest import mock
from typing import Callable
from .main import cryptocurrency_action


@pytest.fixture()
def mock_exchange_rate() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mock_exchange:
        yield mock_exchange


def test_is_not_that_much_for_buy(mock_exchange_rate: Callable) -> None:
    mock_exchange_rate.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_is_not_that_much_for_sell(mock_exchange_rate: Callable) -> None:
    mock_exchange_rate.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_rate_is_more_than_5_percent_higher(
        mock_exchange_rate: Callable
) -> None:
    mock_exchange_rate.return_value = 1.1
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_rate_is_more_than_5_percent_lower(
        mock_exchange_rate: Callable
) -> None:
    mock_exchange_rate.return_value = 0.9
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
