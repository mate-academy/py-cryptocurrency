from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_crypto(mock_predict: int) -> None:
    mock_predict.return_value = 147
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_crypto(mock_predict: int) -> None:
    mock_predict.return_value = 66
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_hodl(mock_predict: int) -> None:
    mock_predict.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_hodl_2(mock_predict: int) -> None:
    mock_predict.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
