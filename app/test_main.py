from typing import Callable
from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_rate_is_growing_more_than5(
    mocked_exchange_rate: Callable,
) -> bool:
    mocked_exchange_rate.return_value = 10
    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_rate_is_decreasing_more_than5(
    mocked_exchange_rate: Callable,
) -> bool:
    mocked_exchange_rate.return_value = 1
    assert cryptocurrency_action(5) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_rate_is_growing_less_then_5(
    mocked_exchange_rate: Callable,
) -> bool:
    mocked_exchange_rate.return_value = 5.25
    assert cryptocurrency_action(5) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_rate_is_decreasing_less_then_5(
    mocked_exchange_rate: Callable,
) -> bool:
    mocked_exchange_rate.return_value = 4.75
    assert cryptocurrency_action(5) == "Do nothing"
