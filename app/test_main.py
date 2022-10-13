from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_crypto(mocked_prediction: [int, float]) -> None:
    mocked_prediction.return_value = 4.7
    assert cryptocurrency_action(5) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_crypto(mocked_prediction: [int, float]) -> None:
    mocked_prediction.return_value = 5.30
    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_crypto_max(mocked_prediction: [int, float]) -> None:
    mocked_prediction.return_value = 5.25
    assert cryptocurrency_action(5) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_crypto_min(mocked_prediction: [int, float]) -> None:
    mocked_prediction.return_value = 4.75
    assert cryptocurrency_action(5) == "Do nothing"
