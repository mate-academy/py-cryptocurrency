# write your code here
from unittest.mock import patch
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        (100, 105.1, "Buy more cryptocurrency"),
        (100, 105.0, "Do nothing"),
        (100, 100.0, "Do nothing"),
        (100, 95.0, "Do nothing"),
        (100, 94.9, "Sell all your cryptocurrency"),
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction: patch,
    current_rate: float,
    prediction_rate: float,
    expected: str,
) -> None:
    mock_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
