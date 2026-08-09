import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,exchange_rate,result",
    [
        (1.5, 3.5, "Buy more cryptocurrency"),
        (60, 40, "Sell all your cryptocurrency"),
        (10, 10.5, "Do nothing"),
        (10, 9.5, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        current_rate: int | float,
        exchange_rate: int | float,
        result: str
) -> None:
    with (
        mock.patch("app.main.get_exchange_rate_prediction")
        as mock_get_exchange
    ):
        mock_get_exchange.return_value = exchange_rate
        assert cryptocurrency_action(current_rate) == result
