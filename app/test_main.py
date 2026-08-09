import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, expect_rate, action", [
    (100, 105.1, "Buy more cryptocurrency"),
    (100, 94.9, "Sell all your cryptocurrency"),
    (100, 105, "Do nothing"),
    (100, 95, "Do nothing"),
    (100, 102, "Do nothing"),
    (100, 98, "Do nothing"),
])
def test_cryptocurrency_action(current_rate: any, expect_rate: any,
                               action: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=expect_rate):
        assert cryptocurrency_action(current_rate) == action
