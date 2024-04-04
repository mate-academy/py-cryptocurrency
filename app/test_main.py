import pytest
from app.main import cryptocurrency_action
from unittest.mock import patch


@pytest.mark.parametrize("current_rate, prediction_rate, expected_action", [
    (100, 110, "Buy more cryptocurrency"),
    (100, 90, "Sell all your cryptocurrency"),
    (100, 105, "Do nothing"),
    (100, 95, "Do nothing")
])
def test_cryptocurrency_action(current_rate: int,
                               prediction_rate: int,
                               expected_action: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=prediction_rate):
        assert cryptocurrency_action(current_rate) == expected_action
