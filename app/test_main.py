from unittest import mock
import app.main


def test_cryptocurrency_action_buy() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_exchange:
        mocked_exchange.return_value = 106
        assert app.main.cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_exchange:
        mocked_exchange.return_value = 94
        assert app.main.cryptocurrency_action(100) == (
            "Sell all your cryptocurrency"
        )


def test_cryptocurrency_action_do_nothing() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_exchange:
        mocked_exchange.return_value = 95
        assert app.main.cryptocurrency_action(100) == (
            "Do nothing"
        )
        mocked_exchange.return_value = 105
        assert app.main.cryptocurrency_action(100) == (
            "Do nothing"
        )
