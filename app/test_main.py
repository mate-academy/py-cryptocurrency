from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, prediction",
    [
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 101, "Do nothing"),
        (100, 99, "Do nothing"),
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
    ]
)
def test_get_exchange_rate_prediction(current_rate, predicted_rate, prediction):
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=predicted_rate):
        assert cryptocurrency_action(current_rate) == prediction
