from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more(get_exchange_rate_prediction: mock) -> None:
    get_exchange_rate_prediction.return_value = 1060
    assert cryptocurrency_action(1000) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all(get_exchange_rate_prediction: mock) -> None:
    get_exchange_rate_prediction.return_value = 940
    assert cryptocurrency_action(1000) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(get_exchange_rate_prediction: mock) -> None:
    get_exchange_rate_prediction.return_value = 950
    assert cryptocurrency_action(1000) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_higher_rate(get_exchange_rate_prediction: mock) -> None:
    get_exchange_rate_prediction.return_value = 1050
    assert cryptocurrency_action(1000) == "Do nothing"
