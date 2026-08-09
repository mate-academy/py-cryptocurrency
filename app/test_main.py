from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 10.6
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all(mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 9.4
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_min(mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_max(mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"
