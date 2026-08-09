import pytest

from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, result",
    [
        (3.1, 5.2, "Buy more cryptocurrency"),
        (5.1, 3.2, "Sell all your cryptocurrency"),
        (5.0, 5.25, "Do nothing"),
        (5.0, 4.75, "Do nothing")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        exchange_rate_prediction: callable,
        current_rate: float,
        prediction_rate: float,
        result: str
) -> None:
    exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
