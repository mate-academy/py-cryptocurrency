from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 107, "Buy more cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
        (50, 35, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing")
    ]
)
def test_cryptocurrency_action(current_rate: int,
                               predicted_rate: int,
                               expected_action: str) -> None:

    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=predicted_rate):
        assert cryptocurrency_action(current_rate) == expected_action
