from unittest import mock
import pytest


from app.main import cryptocurrency_action


actual_rate = 1.00


@pytest.mark.parametrize(
    "today_rate,tomorrow_rate,result",
    [
        (actual_rate, 0.50, "Sell all your cryptocurrency"),
        (actual_rate, 2.25, "Buy more cryptocurrency"),
        (actual_rate, 1.00, "Do nothing"),
        (actual_rate, 1.05, "Do nothing"),
        (actual_rate, 0.95, "Do nothing")
    ]
)
def test_exchange_rate_less_than_actual(today_rate: float,
                                        tomorrow_rate: float,
                                        result: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as rate:
        rate.return_value = tomorrow_rate
        assert cryptocurrency_action(today_rate) == result
