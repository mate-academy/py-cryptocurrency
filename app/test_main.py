from unittest.mock import patch

from .main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_more_5(
        get_exchange_rate_prediction: float
) -> None:
    get_exchange_rate_prediction.return_value = 1.0
    assert (
        cryptocurrency_action(0.9) == "Buy more cryptocurrency"
    )


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_less_5(
        get_exchange_rate_prediction: float
) -> None:
    get_exchange_rate_prediction.return_value = 1.0
    assert (
        cryptocurrency_action(1.4) == "Sell all your cryptocurrency"
    )


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_nothing(
        get_exchange_rate_prediction: float
) -> None:
    get_exchange_rate_prediction.return_value = 1.05
    assert (
        cryptocurrency_action(1.0) == "Do nothing"
    )


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_nothing_2(
        get_exchange_rate_prediction: float
) -> None:
    get_exchange_rate_prediction.return_value = 0.95
    assert (
        cryptocurrency_action(1.0) == "Do nothing"
    )
