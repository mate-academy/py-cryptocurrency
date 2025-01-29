from app.main import cryptocurrency_action
import pytest
from unittest.mock import patch


@pytest.mark.parametrize("current_rate, predicted_rate, expected", [
    (100, 106, "Buy more cryptocurrency"),
    (100, 94, "Sell all your cryptocurrency"),
    (100, 105, "Do nothing"),
    (100, 95, "Do nothing"),
    (100, 100, "Do nothing"),
    (200, 210, "Do nothing"),
    (200, 189, "Sell all your cryptocurrency"),
])
def test_cryptocurrency_action(current_rate: int,
                               predicted_rate: int,
                               expected: str
                               ) -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=predicted_rate):
        assert cryptocurrency_action(current_rate) == expected
