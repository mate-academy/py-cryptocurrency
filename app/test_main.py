from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, result",
    [
        (100, 100, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 106, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction(
        moke_get_exchange_rate_prediction: mock,
        current_rate: int,
        predicted_rate: int,
        result: str
) -> None:
    moke_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == result
