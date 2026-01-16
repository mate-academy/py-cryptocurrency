from unittest.mock import MagicMock

from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_function_gives_positive_prediction(
        get_rate_prediction: MagicMock
) -> None:
    get_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_function_do_nothing_upper_threshold(
        get_rate_prediction: MagicMock
) -> None:
    get_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_function_do_nothing_bottom_threshold(
        get_rate_prediction: MagicMock
) -> None:
    get_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_function_negative_prediction(
        get_rate_prediction: MagicMock
) -> None:
    get_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
