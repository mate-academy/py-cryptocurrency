from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy_more(
        mocked_get_exchange_rate_prediction: float
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 5.1
    assert cryptocurrency_action(4.8) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_sell(
        mocked_get_exchange_rate_prediction: float
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 3
    assert cryptocurrency_action(3.2) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing(
        mocked_get_exchange_rate_prediction: float
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 5.25
    assert cryptocurrency_action(5) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_(
        mocked_get_exchange_rate_prediction: float
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 4.75
    assert cryptocurrency_action(5) == "Do nothing"
