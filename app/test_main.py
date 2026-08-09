from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        (1.00, 1.06, "Buy more cryptocurrency"),
        (1.00, 1.05, "Do nothing"),
        (1.05, 1.00, "Do nothing"),
        (1.01, 1.00, "Do nothing"),
        (1.00, 0.95, "Do nothing"),
        (1.00, 0.75, "Sell all your cryptocurrency"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_get_exchange_rate_prediction: callable,
    current_rate: float,
    predicted_rate: float,
    expected_result: str,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = predicted_rate
    value = cryptocurrency_action(current_rate)

    assert value == expected_result
