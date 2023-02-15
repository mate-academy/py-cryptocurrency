from unittest import mock

import pytest

from .main import cryptocurrency_action


@pytest.mark.parametrize(
    "rate, result",
    [
        (0.94, "Sell all your cryptocurrency"),
        (0.95, "Do nothing"),
        (1.05, "Do nothing"),
        (1.10, "Buy more cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_exchange_rate_more_105_percent(
        mocked_exchange: mock,
        rate: float,
        result: str
) -> None:
    mocked_exchange.return_value = rate
    assert cryptocurrency_action(1) == result
