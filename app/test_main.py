from unittest import mock
import pytest

from app.main import cryptocurrency_action


def test_buy_more() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=200):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=90):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@pytest.mark.parametrize("prediction_rate",
                         [95, 105],
                         ids=[
                             "prediction_rate / current_rate = 0.95",
                             "prediction_rate / current_rate = 1.05"
                         ])
def test_do_nothing(prediction_rate: int) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=prediction_rate):
        assert cryptocurrency_action(100) == "Do nothing"
