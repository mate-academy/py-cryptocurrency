from typing import Union
from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "current_rate,expected_rate,expected_result",
    [
        pytest.param(
            1.9,
            2.5,
            "Buy more cryptocurrency",
            id="function should return Buy more cryptocurrency1"
        ),
        pytest.param(
            1,
            1.05,
            "Do nothing",
            id="function should return Do nothing"
        ),
        pytest.param(
            1,
            0.95,
            "Do nothing",
            id="function should return Do nothing5"
        ),
        pytest.param(
            1.5,
            1,
            "Sell all your cryptocurrency",
            id="function should return Sell all your cryptocurrency4"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_function(
        mock_get_exchange_rate_prediction: mock.Mock,
        current_rate: Union[int, float],
        expected_rate: Union[int, float],
        expected_result: str) -> None:
    mock_get_exchange_rate_prediction.return_value = expected_rate
    assert cryptocurrency_action(current_rate) == expected_result
