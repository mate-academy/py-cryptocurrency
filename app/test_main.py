from app.main import cryptocurrency_action

from unittest import mock

from typing import Any


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
        mock_prediction: Any
) -> None:
    mock_prediction.return_value = 1.06

    current_rate = 1.0
    action = cryptocurrency_action(current_rate)
    assert action == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_your_cryptocurrency(
        mock_prediction: Any
) -> None:
    mock_prediction.return_value = 0.94

    current_rate = 1.0
    action = cryptocurrency_action(current_rate)
    assert action == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_div_current_is_095(
        mock_prediction: Any
) -> None:
    mock_prediction.return_value = 0.95

    current_rate = 1.0
    action = cryptocurrency_action(current_rate)
    assert action == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_div_current_is_105(
        mock_prediction: Any
) -> None:
    mock_prediction.return_value = 1.05

    current_rate = 1.0
    action = cryptocurrency_action(current_rate)
    assert action == "Do nothing"
