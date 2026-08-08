import pytest

from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction, expected",
    [
        (100.0, 105.1, "Buy more cryptocurrency"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 100.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 94.9, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
        current_rate: float,
        prediction: float,
        expected: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = prediction
        result = cryptocurrency_action(current_rate)
        assert result == expected
