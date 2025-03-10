from unittest.mock import patch
from pytest import mark
from typing import Union

from app.main import cryptocurrency_action


@mark.parametrize(
    "current_rate,predicted_rate,expected",
    [
        (100, 101.00, "Do nothing"),
        (100, 105.00, "Do nothing"),
        (100, 106.00, "Buy more cryptocurrency"),
        (100, 99.00, "Do nothing"),
        (100, 95.00, "Do nothing"),
        (100, 94.00, "Sell all your cryptocurrency"),
        (100, 1000.00, "Buy more cryptocurrency"),
        (100, 100.00, "Do nothing"),
        (100, 0.00, "Sell all your cryptocurrency"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_with_various_conditions(
        mocked_get_exchange_rate_prediction: callable,
        current_rate: Union[int, float],
        predicted_rate: float,
        expected: str,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected
