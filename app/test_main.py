from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_if_difference_105(
        mocked_prediction: int) -> None:
    mocked_prediction.return_value = 3.15
    assert cryptocurrency_action(3) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_if_difference_95(
        mocked_prediction: int) -> None:
    mocked_prediction.return_value = 4.75
    assert cryptocurrency_action(5) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy_more_cryptocurrency(
        mocked_prediction: int) -> None:
    mocked_prediction.return_value = 3
    assert cryptocurrency_action(2.85) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_sell_all_your_cryptocurrency(
        mocked_prediction: int) -> None:
    mocked_prediction.return_value = 2.75
    assert cryptocurrency_action(3) == "Sell all your cryptocurrency"
