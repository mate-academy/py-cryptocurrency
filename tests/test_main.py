from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_growth_higher_five_percent(mocked_get_exchange_rate_prediction):
    mocked_get_exchange_rate_prediction.return_value = 41870

    assert cryptocurrency_action(39876) == "Buy more cryptocurrency"
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_decline_lower_five_percent(mocked_get_exchange_rate_prediction):
    mocked_get_exchange_rate_prediction.return_value = 41870

    assert cryptocurrency_action(44074) == "Sell all your cryptocurrency"
    assert cryptocurrency_action(60000) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_difference_is_not_that_much(mocked_get_exchange_rate_prediction):
    mocked_get_exchange_rate_prediction.return_value = 41870

    assert cryptocurrency_action(39877) == "Do nothing"
    assert cryptocurrency_action(44073) == "Do nothing"
