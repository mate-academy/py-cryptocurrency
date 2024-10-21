from unittest.mock import patch, Mock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_get_prediction: Mock) -> None:
    current_rate = 100
    mock_get_prediction.return_value = 105
    res = cryptocurrency_action(current_rate)
    assert res == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all(mock_get_prediction: Mock) -> None:
    current_rate = 100
    mock_get_prediction.return_value = 95
    res = cryptocurrency_action(current_rate)
    assert res == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_get_prediction: Mock) -> None:
    current_rate = 100
    mock_get_prediction.return_value = 103
    res = cryptocurrency_action(current_rate)
    assert res == "Do nothing"
