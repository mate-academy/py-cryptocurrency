from unittest import mock
import pytest
from app.main import cryptocurrency_action
from typing import Union


@pytest.mark.parametrize(
    "current_rate, rate_prediction, expected",
    [
        pytest.param(
            1,
            1.05,
            "Do nothing",
            id="exchange rate less then 5% to buy"),
        pytest.param(
            1,
            0.95,
            "Do nothing",
            id="exchange rate less then 5% to sell"),
        pytest.param(
            2,
            1.5,
            "Sell all your cryptocurrency",
            id="exchange rate < 5%  from current"),
        pytest.param(
            2.06,
            3,
            "Buy more cryptocurrency",
            id="exchange rate > 5% from current")
    ]

)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: Union[int, float],
        current_rate: Union[int, float],
        rate_prediction: Union[int, float],
        expected: str) -> None:
    mock_get_exchange_rate_prediction.return_value = rate_prediction
    assert cryptocurrency_action(current_rate) == expected
