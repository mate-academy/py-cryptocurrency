from app.main import cryptocurrency_action
import pytest
from unittest.mock import patch


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (2, 1, "Buy more cryptocurrency"),
        (1, 2, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),
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
