from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "rate,return_value,result",
    [
        (50, 100, "Buy more cryptocurrency"),
        (70, 112, "Buy more cryptocurrency"),
        (90, 99, "Buy more cryptocurrency"),
        (90, 50, "Sell all your cryptocurrency"),
        (70, 34, "Sell all your cryptocurrency"),
        (70, 72, "Do nothing"),
        (55, 54, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        rate: int,
        return_value: int,
        result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_exchange:
        mock_exchange.return_value = return_value
        assert cryptocurrency_action(rate) == result
