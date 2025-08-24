import pytest
from app.main import cryptocurrency_action
from unittest import mock

@pytest.mark.parametrize(
    "prediction_rate,expected",
    [
        [11, "Buy more cryptocurrency"],
        [10.6, "Buy more cryptocurrency"],
        [10.5, "Do nothing"],
        [9.5, "Do nothing"],
        [9.4, "Sell all your cryptocurrency"],
        [5, "Sell all your cryptocurrency"]
    ]
)
def test_buy_and_sell_currency_correctly(
        prediction_rate: int | float,
        expected: str
) -> None:
    current_rate = 10
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=prediction_rate):
        assert cryptocurrency_action(current_rate) == expected