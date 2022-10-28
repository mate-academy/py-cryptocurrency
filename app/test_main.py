from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_function_return_more_1_05(mocked_exchange: callable) -> None:
    mocked_exchange.return_value = 1.3
    current_rate = 1
    cryptocurrency_action(current_rate)
    mocked_exchange.assert_called_once()
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_function_return_less_0_95(mocked_exchange: callable) -> None:
    mocked_exchange.return_value = 1.2
    current_rate = 3
    cryptocurrency_action(current_rate)
    mocked_exchange.assert_called_once()
    assert cryptocurrency_action(current_rate) == \
           "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_function_do_nothing_with_1_05(mocked_exchange: callable) -> None:
    mocked_exchange.return_value = 1.05
    current_rate = 1
    cryptocurrency_action(current_rate)
    mocked_exchange.assert_called_once()
    assert cryptocurrency_action(current_rate) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_function_do_nothing_with_0_95(mocked_exchange: callable) -> None:
    mocked_exchange.return_value = 0.95
    current_rate = 1
    cryptocurrency_action(current_rate)
    mocked_exchange.assert_called_once()
    assert cryptocurrency_action(current_rate) == "Do nothing"
