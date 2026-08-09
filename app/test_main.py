from app.main import cryptocurrency_action
from unittest import mock
from typing import Union


@mock.patch("app.main.get_exchange_rate_prediction")
def test_the_rate_has_increased(expected_rate: Union[int, float]) -> None:
    expected_rate.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_the_rate_has_loss(expected_rate: Union[int, float]) -> None:
    expected_rate.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_the_rate_has_not_change(expected_rate: Union[int, float]) -> None:
    expected_rate.return_value = 100
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_the_rate_has_not_increased(expected_rate: Union[int, float]) -> None:
    expected_rate.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_the_rate_has_not_loss(expected_rate: Union[int, float]) -> None:
    expected_rate.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
