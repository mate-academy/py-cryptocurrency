from typing import Union
from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected",
    [
        pytest.param(
            2,
            1,
            "Buy more cryptocurrency",
            id="higher_rate"
        ),
        pytest.param(
            1.06,
            1,
            "Buy more cryptocurrency",
            id="bound_higher"
        ),
        pytest.param(
            0.5,
            1,
            "Sell all your cryptocurrency",
            id="lower_rate"
        ),
        pytest.param(
            0.94,
            1,
            "Sell all your cryptocurrency",
            id="bound_lower"
        ),
        pytest.param(
            1.05,
            1,
            "Do nothing",
            id="same_rate"
        ),
        pytest.param(
            0.95,
            1,
            "Do nothing",
            id="same_rate"
        ),
        pytest.param(
            1,
            1,
            "Do nothing",
            id="same_rate"
        ),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        get_exchange_rate_prediction: float,
        prediction_rate: float,
        current_rate: Union[int, float],
        expected: str
) -> None:
    get_exchange_rate_prediction.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected
