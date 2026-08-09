from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_crypto_buy(mocked_exchange: int) -> None:
    mocked_exchange.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_crypto_sell(mocked_exchange: int) -> None:
    mocked_exchange.return_value = 60
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_crypto_nothing_when_negative(mocked_exchange: int) -> None:
    mocked_exchange.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_crypto_nothing_when_positive(mocked_exchange: int) -> None:
    mocked_exchange.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
