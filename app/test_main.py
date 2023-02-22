from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_crypto(mocked_exchange: type) -> None:
    current_rate = 100
    mocked_exchange.return_value = current_rate * 1.06

    cryptocurrency_action(current_rate)

    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_crypto(mocked_exchange: type) -> None:
    current_rate = 100
    mocked_exchange.return_value = current_rate * 0.94

    cryptocurrency_action(current_rate)

    result = "Sell all your cryptocurrency"
    assert cryptocurrency_action(current_rate) == result


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_if_rate_percent_is_105(mocked_exchange: type) -> None:
    current_rate = 100
    mocked_exchange.return_value = current_rate * 1.05

    cryptocurrency_action(current_rate)

    assert cryptocurrency_action(current_rate) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_if_rate_percent_is_95(mocked_exchange: type) -> None:
    current_rate = 100
    mocked_exchange.return_value = current_rate * 0.95

    cryptocurrency_action(current_rate)

    assert cryptocurrency_action(current_rate) == "Do nothing"
