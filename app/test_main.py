from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (1000, 1200, "Buy more cryptocurrency"),
        (1000, 949, "Sell all your cryptocurrency"),
        (1000, 950, "Do nothing"),
        (1000, 1050, "Do nothing")
    ]
)
def test_cryptocurrency_action(
    current_rate: float, prediction_rate: float, expected: str
) -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction", return_value=prediction_rate
    ):
        assert cryptocurrency_action(current_rate) == expected
