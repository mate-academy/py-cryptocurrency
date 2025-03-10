import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (100, 105.5, "Buy more cryptocurrency"),
        (100, 112.2, "Buy more cryptocurrency"),
        (100, 94.5, "Sell all your cryptocurrency"),
        (100, 91.0, "Sell all your cryptocurrency"),
        (100, 103.0, "Do nothing"),
        (100, 97.5, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        current_rate: float,
        prediction_rate: float,
        expected: str) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = prediction_rate

        result = cryptocurrency_action(current_rate)
        assert result == expected
