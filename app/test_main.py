# write your code here
from unittest import mock
from unittest.mock import Mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy_if_grow_rate_more_than_5_percent(
        mocked_get_exchange_rate_prediction: Mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 6

    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_if_grow_rate_less_than_5_percent(
        mocked_get_exchange_rate_prediction: Mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 5.1

    assert cryptocurrency_action(5) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_if_grow_rate_equal_5_percent(
        mocked_get_exchange_rate_prediction: Mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 5.25

    assert cryptocurrency_action(5) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_sell_if_drop_rate_more_than_5_percent(
        mocked_get_exchange_rate_prediction: Mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 4.2

    assert cryptocurrency_action(5) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_if_drop_rate_less_than_5_percent(
        mocked_get_exchange_rate_prediction: Mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 4.9

    assert cryptocurrency_action(5) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_if_drop_rate_equal_5_percent(
        mocked_get_exchange_rate_prediction: Mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 4.75

    assert cryptocurrency_action(5) == "Do nothing"
