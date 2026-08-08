from unittest import mock
from typing import Any
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_main_do_nothing_1_05(value: Any) -> None:
    value.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_main_do_nothing_0_95(value: Any) -> None:
    value.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
