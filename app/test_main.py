from unittest import mock
import pytest

from typing import Callable

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mock_prediction:
        yield mock_prediction


def test_should_raise_type_error_when_current_rate_is_string() -> None:
    with pytest.raises(TypeError):
        cryptocurrency_action("16")


def test_not_enough_to_buy(mock_rate_prediction: Callable) -> None:
    mock_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_not_enough_to_sell(mock_rate_prediction: Callable) -> None:
    mock_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_return_buy_crypto_when_more_than_5_percent_higher(
        mock_rate_prediction: Callable
) -> None:
    mock_rate_prediction.return_value = 1.1
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_return_sell_crypto_when_more_than_5_percent_lower(
        mock_rate_prediction: Callable
) -> None:
    mock_rate_prediction.return_value = 0.9
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"