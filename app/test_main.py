import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        (100, 105.1, "Buy more cryptocurrency"),
        (100, 94.8, "Sell all your cryptocurrency"),
        (100, 102.0, "Do nothing"),
        (100, 105.0, "Do nothing"),
        (100, 95.0, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        current_rate: float,
        predicted_rate: float,
        expected_result: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)
        assert result == expected_result
