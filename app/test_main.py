import pytest
from typing import Union
from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate,predicted_rate,expected_result", [
    (100, 101, "Do nothing"),
    (100, 93, "Sell all your cryptocurrency"),
    (100, 106, "Buy more cryptocurrency"),
    (100, 105, "Do nothing"),
    (100, 95, "Do nothing"),
])
def test_is_action_correct(
        current_rate: Union[int, float],
        predicted_rate: float,
        expected_result: str
) -> None:
    with (patch("app.main.get_exchange_rate_prediction")
          as mock_exchange_prediction):
        mock_exchange_prediction.return_value = predicted_rate
        assert cryptocurrency_action(current_rate) == expected_result
