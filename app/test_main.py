import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "mock_prediction_value, current_rate, expected_result",
    [
        (105.01, 100, "Buy more cryptocurrency"),  # Predicted rate > 5% higher
        (94.99, 100, "Sell all your cryptocurrency"),
        (105.0, 100, "Do nothing"),  # Predicted rate exactly 5% higher
        (95.0, 100, "Do nothing"),  # Predicted rate exactly 5% lower
        (102, 100, "Do nothing"),  # Predicted rate within 5%
        (98, 100, "Do nothing"),  # Predicted rate within 5%
    ]
)
def test_cryptocurrency_action(
    mock_prediction_value: float, current_rate: float, expected_result: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = mock_prediction_value
        result = cryptocurrency_action(current_rate)
        assert result == expected_result, (
            f"Expected '{expected_result}' but got '{result}' for "
            f"prediction {mock_prediction_value} "
            f"and current rate {current_rate}."
        )
