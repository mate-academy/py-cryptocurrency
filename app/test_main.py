import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate, result",
    [
        (120, "Buy more cryptocurrency"),
        (80, "Sell all your cryptocurrency"),
        (105, "Do nothing"),
        (95, "Do nothing")
    ]
)
def test_cryptocurrency_action(predicted_rate: int, result: str) -> None:
    current_rate = 100
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=predicted_rate
    ):
        assert cryptocurrency_action(current_rate) == result
