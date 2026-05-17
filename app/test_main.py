import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 105.01, "Buy more cryptocurrency"),
        (100, 91, "Sell all your cryptocurrency"),
        (100, 94.99, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_prediction: int, current_rate: int,
                               predicted_rate: int, expected: str) -> None:
    mock_get_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected
