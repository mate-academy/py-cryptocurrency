from typing import Union
import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 105.01, "Buy more cryptocurrency"),
        (100, 94.99, "Sell all your cryptocurrency"),
        (100, 104.99, "Do nothing"),
        (100, 95.01, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        current_rate: Union[int, float],
        predicted_rate: Union[int, float],
        expected: str
) -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=predicted_rate
    ):
        assert cryptocurrency_action(current_rate) == expected


def test_do_nothing_on_exactly_5_percent_increase() -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=105.0
    ):
        assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_on_exactly_5_percent_decrease() -> None:
    with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=95.0
    ):
        assert cryptocurrency_action(100) == "Do nothing"  #
