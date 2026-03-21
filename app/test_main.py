from unittest import mock
from typing import Union
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 105.0, "Do nothing"),
        (100, 105.01, "Buy more cryptocurrency"),
        (100, 200.0, "Buy more cryptocurrency"),
        (100, 95.0, "Do nothing"),
        (100, 94.99, "Sell all your cryptocurrency"),
        (100, 10.0, "Sell all your cryptocurrency"),
        (100, 100.0, "Do nothing"),
        (50.0, 53.0, "Buy more cryptocurrency"),
        (50.0, 47.0, "Sell all your cryptocurrency"),
        (50.0, 50.0, "Do nothing")
    ]
)
def test_get_exchange_rate_prediction(current_rate: Union[int, float],
                                      predicted_rate: Union[int, float],
                                      expected: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=predicted_rate):
        assert cryptocurrency_action(current_rate) == expected
