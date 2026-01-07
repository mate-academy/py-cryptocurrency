from unittest import mock
from app.main import cryptocurrency_action
from typing import Union


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_buy_when_prediction_increase(
        mocked_rate: Union[int, float]
) -> None:
    mocked_rate.return_value = 120
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_sell_when_prediction_decrease(
        mocked_rate: Union[int, float]
) -> None:
    mocked_rate.return_value = 90
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exact_upper_boundary(
        mocked_rate: Union[int, float]
) -> None:
    mocked_rate.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exact_lower_boundary(
    mocked_rate: Union[int, float]
) -> None:
    mocked_rate.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
