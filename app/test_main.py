import pytest
from unittest import mock
from app.main import cryptocurrency_action


def test_cryptocurrency_action_buy_more_cryptocurrency_result() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
         as exchange_prediction:
        exchange_prediction.return_value = 7
        assert cryptocurrency_action(5) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell_all_cryptocurrency_result() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
         as exchange_prediction:
        exchange_prediction.return_value = 4
        assert cryptocurrency_action(5) == "Sell all your cryptocurrency"


@pytest.mark.parametrize(
    "prediction_rate,current_rate,result",
    [
        (5.25, 5, "Do nothing"), (4.75, 5, "Do nothing"), (5, 5, "Do nothing")
    ]
)
def test_cryptocurrency_action_do_nothing_result(
    prediction_rate: int, current_rate: int, result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
         as exchange_prediction:
        exchange_prediction.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == result
