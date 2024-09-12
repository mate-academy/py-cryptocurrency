from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_check_crypto_buy(mock_predict: int) -> None:
    mock_predict.return_value = 200
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_check_crypto_sell(mock_predict: int) -> None:
    mock_predict.return_value = 20
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_check_crypto_hold(mock_predict: int) -> None:
    mock_predict.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_check_crypto_holdx2(mock_predict: int) -> None:
    mock_predict.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
