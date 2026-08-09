import pytest
from unittest.mock import patch
from .main import cryptocurrency_action
from typing import Union


@pytest.mark.parametrize(
    "current_rate, rate_prediction, expected",
    [
        pytest.param(
            100, 105,
            "Do nothing", id="exchange rate exactly 5% higher, do nothing"
        ),
        pytest.param(
            100, 95,
            "Do nothing", id="exchange rate exactly 5% lower, do nothing"
        ),
        pytest.param(
            100,
            94,
            "Sell all your cryptocurrency",
            id="exchange rate more than 5% lower, sell",
        ),
        pytest.param(
            100,
            106,
            "Buy more cryptocurrency",
            id="exchange rate more than 5% higher, buy",
        ),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: patch,
    current_rate: Union[int, float],
    rate_prediction: Union[int, float],
    expected: str,
) -> None:
    mock_get_exchange_rate_prediction.return_value = rate_prediction
    assert cryptocurrency_action(current_rate) == expected
