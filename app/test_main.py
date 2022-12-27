from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_crypto(mocked_prediction: callable) -> None:
    mocked_prediction.return_value = 8.12
    assert cryptocurrency_action(23) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_crypto(mocked_prediction: callable) -> None:
    mocked_prediction.return_value = 88.92
    assert cryptocurrency_action(45) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mocked_prediction: callable) -> None:
    mocked_prediction.return_value = 100
    assert cryptocurrency_action(101) == "Do nothing"
