import pytest
from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, exchange_rate ,expected_result", [
    (0.95, 1.007, "Buy more cryptocurrency"),
    (1.05, 0.9765, "Sell all your cryptocurrency"),
    (1.0, 1.035, "Do nothing"),
    (100, 95, "Do nothing"),
    (1.0, 1.05, "Do nothing")
])
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: patch,
        current_rate: float,
        exchange_rate: float,
        expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == expected_result