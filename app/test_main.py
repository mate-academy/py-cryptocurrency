import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate,predicted_rate,expected", [
    (100.0, 107.0, "Buy more cryptocurrency"),
    (100.0, 93.0, "Sell all your cryptocurrency"),
    (100.0, 103.0, "Do nothing"),
    (100.0, 105.0, "Do nothing"),
    (100.0, 95.0, "Do nothing"),
])
def test_cryptocurrency_action(current_rate: int | float,
                               predicted_rate: int | float,
                               expected: str) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_get_prediction:
        mock_get_prediction.return_value = predicted_rate
        result = cryptocurrency_action(current_rate)
        assert result == expected
