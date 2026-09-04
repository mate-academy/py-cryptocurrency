# write your code here
from unittest import mock

from app.main import cryptocurrency_action

current_rate = 1


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_recommendation_when_rate_is_high(
        mocked_get_exchange_rate_prediction: object
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_recommendation_when_rate_equals_5_percent_higher(
        mocked_get_exchange_rate_prediction: object
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(current_rate) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_recommendation_when_difference_is_low(
        mocked_get_exchange_rate_prediction: object
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(current_rate) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_recommendation_when_rate_equals_5_percent_lower(
        mocked_get_exchange_rate_prediction: object
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(current_rate) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_recommendation_when_rate_is_low(
        mocked_get_exchange_rate_prediction: object
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.9
    assert cryptocurrency_action(current_rate) == ("Sell all "
                                                   "your cryptocurrency")
