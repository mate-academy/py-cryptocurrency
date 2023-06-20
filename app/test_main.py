from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, result",
    [
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing"),
        (2, 1, "Buy more cryptocurrency"),
        (1, 2, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_mocked_get_exchange_rate_prediction_with_1_05(
    mocked_function,
    prediction_rate,
    current_rate,
    result
):
    mocked_function.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
