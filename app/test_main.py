from app.main import cryptocurrency_action
import pytest
from unittest.mock import patch


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (1, 2, "Buy more cryptocurrency"),
        (2, 1, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),
        (10, 9.5, "Do nothing"),
        (10, 10.5, "Do nothing"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: int,
        current_rate: int,
        prediction_rate: int,
        expected: str,
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
