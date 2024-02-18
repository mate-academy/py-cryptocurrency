from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.07)
def test_cryptocurrency_should_buy_more_cryptocurrency(
        mocked_exchange: any) -> None:
    assert (
        cryptocurrency_action(1) == "Buy more cryptocurrency"
    )
    mocked_exchange.assert_called_once_with(1)


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.93)
def test_cryptocurrency_should_sell_all_your_cryptocurrency(
        mocked_exchange: any) -> None:
    assert (
        cryptocurrency_action(1) == "Sell all your cryptocurrency"
    )
    mocked_exchange.assert_called_once_with(1)


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.05)
def test_cryptocurrency_should_do_nothing_1(
        mocked_exchange: any) -> None:
    assert (
        cryptocurrency_action(1) == "Do nothing"
    )
    mocked_exchange.assert_called_once_with(1)


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.95)
def test_cryptocurrency_should_do_nothing_2(
        mocked_exchange: any) -> None:
    assert (
        cryptocurrency_action(1) == "Do nothing"
    )
    mocked_exchange.assert_called_once_with(1)
