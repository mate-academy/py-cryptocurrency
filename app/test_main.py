from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.6)
def test_buy_more_cryptocurrency(mocked_get_exchange_rate_prediction: mock) \
        -> None:
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.89)
def test_sell_all_your_crypto(mocked_get_exchange_rate_prediction: mock)\
        -> None:
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.05)
def test_do_nothing_max(mocked_get_exchange_rate_prediction: mock) -> None:
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.95)
def test_do_nothing_min(mocked_get_exchange_rate_prediction: mock) -> None:
    assert cryptocurrency_action(1) == "Do nothing"
