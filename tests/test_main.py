from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency_when_predicted_rate_is_more_than_5_pct_higher(
        mocked_get_exchange_rate_prediction
):
    mocked_get_exchange_rate_prediction.return_value = 117.65

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_predicted_rate_is_exactly_5_pct_higher(
        mocked_get_exchange_rate_prediction
):
    mocked_get_exchange_rate_prediction.return_value = 105

    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_predicted_rate_is_exactly_5_pct_lower(
        mocked_get_exchange_rate_prediction
):
    mocked_get_exchange_rate_prediction.return_value = 95

    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency_when_predicted_rate_is_more_than_5_pct_lower(
        mocked_get_exchange_rate_prediction
):
    mocked_get_exchange_rate_prediction.return_value = 85.6

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
