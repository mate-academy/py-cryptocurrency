import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize("mock_prediction,expected", [
    (105.01, "Buy more cryptocurrency"),
    (104.99, "Do nothing"),
    (95.01, "Do nothing"),
    (94.99, "Sell all your cryptocurrency"),
    (100.0, "Do nothing"),
    (95.0, "Do nothing"),
    (105.0, "Do nothing"),
])
def test_cryptocurrency_action(mock_prediction: float, expected: str) -> None:
    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=mock_prediction
    ):
        assert cryptocurrency_action(100) == expected
