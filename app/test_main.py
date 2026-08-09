from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_sell(mocked_prediction: callable) -> None:
    mocked_prediction.return_value = 3.70
    assert cryptocurrency_action(4) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy(mocked_prediction: callable) -> None:
    mocked_prediction.return_value = 4.30
    assert cryptocurrency_action(4) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_at_min(mocked_prediction: callable) -> None:
    mocked_prediction.return_value = 3.8
    assert cryptocurrency_action(4) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_at_max(mocked_prediction: callable) -> None:
    mocked_prediction.return_value = 4.2
    assert cryptocurrency_action(4) == "Do nothing"
