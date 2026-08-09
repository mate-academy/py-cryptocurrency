from unittest import mock
from typing import Any
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_not_buy_when_prediction_rate_lower_or_equal_to_5_percent_to_high(
        mocked: Any
) -> None:
    mocked.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_not_buy_when_prediction_rate_higher_or_equal_to_5_percent_to_low(
        mocked: Any
) -> None:
    mocked.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_not_buy_when_prediction_rate_higher_than_5_percent(
        mocked: Any
) -> None:
    mocked.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_not_buy_when_prediction_rate_lower_than_5_percent(
        mocked: Any
) -> None:
    mocked.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
