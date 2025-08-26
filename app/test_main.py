import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, predicted_rate, expected_action", [
    (100, 120, "Buy more cryptocurrency"),
    (100, 105.1, "Buy more cryptocurrency"),
    (100, 105, "Do nothing"),
    (100, 100, "Do nothing"),
    (100, 95, "Do nothing"),
    (100, 94.9, "Sell all your cryptocurrency"),
    (100, 80, "Sell all your cryptocurrency")
])
def test_cryptocurrency_action_returns_correct_action(current_rate: int,
                                                      predicted_rate: int,
                                                      expected_action: str
                                                      ) -> None:

    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted_rate):

        assert cryptocurrency_action(current_rate) == expected_action
