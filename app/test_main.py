from unittest import mock
from typing import Any
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_main_do_nothing(value: Any) -> None:
    value.return_value = 10
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_main_sell_all(value: Any) -> None:
    value.return_value = 1
    assert cryptocurrency_action(0) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_main_bye_more(value: Any) -> None:
    value.return_value = 20
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"
