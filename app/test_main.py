from unittest import mock
from app.main import cryptocurrency_action


def test_cryptocurrency_action_buy_more() -> None:
    get_exchange_rate_prediction = mock.MagicMock()
    cryptocurrency_action(1.00)
    get_exchange_rate_prediction.return_value = 1.06

    assert cryptocurrency_action(1.00) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell_all() -> None:
    get_exchange_rate_prediction = mock.MagicMock()
    cryptocurrency_action(1.00)
    get_exchange_rate_prediction.return_value = 0.95

    assert cryptocurrency_action(1.00) == "Sell all your cryptocurrency"
