from unittest.mock import patch
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected",
    [
        (100, 105.01, "Buy more cryptocurrency"),
        (100, 110.0, "Buy more cryptocurrency"),
        (100, 105.0, "Do nothing"),
        (100, 100.0, "Do nothing"),
        (100, 95.0, "Do nothing"),
        (100, 94.99, "Sell all your cryptocurrency"),
        (100, 90.0, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
    current_rate: float,
    predicted_rate: float,
    expected: str,
) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = predicted_rate
        assert cryptocurrency_action(current_rate) == expected
