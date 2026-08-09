from app.main import cryptocurrency_action
from unittest.mock import patch


@patch("app.main.get_exchange_rate_prediction")
def test_should_buy_more_crypto(exchange_rate_mock: float) -> None:
    exchange_rate_mock.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_sell_crypto(exchange_rate_mock: float) -> None:
    exchange_rate_mock.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_for_095(exchange_rate_mock: float) -> None:
    exchange_rate_mock.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_for_105(exchange_rate_mock: float) -> None:
    exchange_rate_mock.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
