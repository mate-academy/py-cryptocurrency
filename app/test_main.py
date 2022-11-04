from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_crypto(mocked_value: int) -> None:
    mocked_value.return_value = 3

    assert cryptocurrency_action(5) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_crypto(mocked_value: int) -> None:
    mocked_value.return_value = 7

    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_if_105(mocked_value: int) -> None:
    mocked_value.return_value = 5.25

    assert cryptocurrency_action(5) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_if_095(mocked_value: int) -> None:
    mocked_value.return_value = 4.75

    assert cryptocurrency_action(5) == "Do nothing"
