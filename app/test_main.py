from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_check_crypto_buy(mock_predict: int) -> None:
    mock_predict.return_value = 5.3
    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_check_crypto_sell(mock_predict: int) -> None:
    mock_predict.return_value = 4.7
    assert cryptocurrency_action(5) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_check_crypto_hold(mock_predict: int) -> None:
    mock_predict.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
