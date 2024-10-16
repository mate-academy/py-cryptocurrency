from app.main import cryptocurrency_action
from unittest import mock


CURRENT_RATE = 1.2


def test_cryptocurrency_action_buy_more() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 1.5
        assert cryptocurrency_action(CURRENT_RATE) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell_all() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 0.8
        assert (
            cryptocurrency_action(CURRENT_RATE)
            == "Sell all your cryptocurrency"
        )


def test_cryptocurrency_action_do_nothing() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 0.9
        assert cryptocurrency_action(CURRENT_RATE) == "Do nothing"
