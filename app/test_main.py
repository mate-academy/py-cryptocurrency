import pytest

from unittest import mock
from typing import Callable

from app.main import cryptocurrency_action


@pytest.fixture
def mock_exchange_rate_prediction() -> Callable:
    with (
        mock.patch("app.main.get_exchange_rate_prediction")
        as mock_get_exchange_rate_prediction
    ):
        yield mock_get_exchange_rate_prediction


def test_cryptocurrency_action_buy_more(
        mock_exchange_rate_prediction: Callable
) -> None:
    mock_exchange_rate_prediction.return_value = 1.1
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell_all(
        mock_exchange_rate_prediction: Callable
) -> None:
    mock_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing(
    mock_exchange_rate_prediction: Callable
) -> None:
    mock_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1.0) == "Do nothing"
    mock_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1.0) == "Do nothing"
