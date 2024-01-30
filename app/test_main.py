import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,exchange_rate,result",
    [
        (1.5, 3.2, "Buy more cryptocurrency"),
        (1.5, 2.3, "Buy more cryptocurrency"),
        (2, 2, "Do nothing"),
        (2.4, 2.6, "Do nothing"),
        (1, 0.5, "Sell all your cryptocurrency"),
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
