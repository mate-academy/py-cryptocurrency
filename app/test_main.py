from unittest.mock import patch, MagicMock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (100, 105.1, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94.9, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction: MagicMock,
        current_rate: float,
        prediction_rate: float,
        expected: str
) -> None:
    mock_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
