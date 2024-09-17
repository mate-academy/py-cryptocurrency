from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_currency(mocked_rate_prediction):
    mocked_rate_prediction.return_value = 10.6

    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_currency(mocked_rate_prediction):
    mocked_rate_prediction.return_value = 9.4

    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_with_smaller_prediction(mocked_rate_prediction):
    mocked_rate_prediction.return_value = 9.5

    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_with_bigger_prediction(mocked_rate_prediction):
    mocked_rate_prediction.return_value = 10.5

    assert cryptocurrency_action(10) == "Do nothing"
