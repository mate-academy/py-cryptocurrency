import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_action",
    [
        (100, 106.01, "Buy more cryptocurrency"),
        (100, 94.99, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 104.99, "Do nothing"),
        (100, 95.01, "Do nothing"),
    ]
)
def test_cryptocurrency_action(current_rate: int | float,
                               prediction_rate: int | float,
                               expected_action: str
                               ) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=prediction_rate
    ):
        assert cryptocurrency_action(current_rate) == expected_action
