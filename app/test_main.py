from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "rate, exchange_predict, result",
    [
        (0.25, 1, "Buy more cryptocurrency"),
        (1, 0.9, "Sell all your cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing")

    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_actions_for_crypto(
        get_exchange: mock,
        rate: int | float,
        exchange_predict: int | float,
        result: str
) -> None:
    get_exchange.return_value = exchange_predict
    assert (
        cryptocurrency_action(rate) == result
    )
