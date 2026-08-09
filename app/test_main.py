from .main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "rate, result",
    [
        (0.92, "Sell all your cryptocurrency"),
        (0.95, "Do nothing"),
        (1.05, "Do nothing"),
        (1.11, "Buy more cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange: mock,
        rate: float,
        result: str
) -> None:
    mocked_exchange.return_value = rate
    assert cryptocurrency_action(1) == result
