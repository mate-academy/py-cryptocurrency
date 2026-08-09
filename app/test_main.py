import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, result",
    [
        (1, 1.2, "Buy more cryptocurrency"),
        (1, 0.9, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_get_exchange: callable,
                               current_rate: int,
                               prediction_rate: int,
                               result: str) -> None:
    mocked_get_exchange.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
