import pytest
from unittest.mock import patch

from .main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,result",
    [
        (1.10, 1, "Buy more cryptocurrency"),
        (0.93, 1, "Sell all your cryptocurrency"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing")
    ]
)
def test_cryptocurrency_action_return_correct_answer(prediction_rate: float,
                                                     current_rate: float,
                                                     result: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=prediction_rate):
        assert cryptocurrency_action(current_rate) == result
