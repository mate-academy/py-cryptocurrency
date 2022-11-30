from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_cryptocurrency(mocked: float) -> None:
    mocked.return_value = 9.3
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_cryptocurrency(mocked: float) -> None:
    mocked.return_value = 10.6
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_current_rate_is_not_low_enough(mocked: float) -> None:
    mocked.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_if_current_rate_is_not_high_enough(mocked: float) -> None:
    mocked.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"
