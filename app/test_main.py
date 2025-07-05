from unittest import mock
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "current_rate, predict_rate, expected",
    [
        (100, 90, "Sell all your cryptocurrency"),
        (100, 120, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
def test_cryptocurrency_action(current_rate: int | float,
                               predict_rate: int | float,
                               expected: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=predict_rate):
        assert cryptocurrency_action(current_rate) == expected
