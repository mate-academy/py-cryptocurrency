from unittest import mock


from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_crypto(mocked_prediction: int) -> None:
    mocked_prediction.return_value = 110
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_crypto(mocked_prediction: int) -> None:
    mocked_prediction.return_value = 92
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mocked_prediction: int) -> None:
    mocked_prediction.return_value = 99
    assert cryptocurrency_action(100) == "Do nothing"
