from app.main import cryptocurrency_action
from unittest.mock import patch
from typing import Callable


@patch("app.main.get_exchange_rate_prediction", return_value=0.94)
def test_sell_when_prediction_decreases_over_5_percent(
    mock_get_prediction: Callable
) -> None:
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=1.06)
def test_buy_when_prediction_increases_over_5_percent(
    mock_get_prediction: Callable
) -> None:
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=0.95)
def test_do_nothing_when_prediction_is_exactly_5_percent_lower(
    mock_get_prediction: Callable
) -> None:
    assert cryptocurrency_action(1.0) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=1.05)
def test_do_nothing_when_prediction_is_exactly_5_percent_higher(
    mock_get_prediction: Callable
) -> None:
    assert cryptocurrency_action(1.0) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=1.0)
def test_do_nothing_when_prediction_is_equal_to_current(
    mock_get_prediction: Callable
) -> None:
    assert cryptocurrency_action(1.0) == "Do nothing"
