from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(
        get_exchange_rate_prediction: float) -> None:
    get_exchange_rate_prediction.return_value = 80
    assert cryptocurrency_action(82) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_more(
        get_exchange_rate_prediction: float) -> None:
    get_exchange_rate_prediction.return_value = 100
    assert cryptocurrency_action(80) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_all(
        get_exchange_rate_prediction: float) -> None:
    get_exchange_rate_prediction.return_value = 80
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_105_percent_do_nothing(
        get_exchange_rate_prediction: float) -> None:
    get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_95_percent_do_nothing(
        get_exchange_rate_prediction: float) -> None:
    get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
