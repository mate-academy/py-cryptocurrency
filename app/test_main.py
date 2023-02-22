from unittest.mock import patch
import app.main as main


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_get_exchange_rate_prediction: None) \
        -> None:
    mock_get_exchange_rate_prediction.return_value = 1.06
    assert main.cryptocurrency_action(1.0) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_get_exchange_rate_prediction: None) \
        -> None:
    mock_get_exchange_rate_prediction.return_value = 0.9
    assert main.cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(mock_get_exchange_rate_prediction: None) \
        -> None:
    mock_get_exchange_rate_prediction.return_value = 1.05
    assert main.cryptocurrency_action(1.0) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(mock_get_exchange_rate_prediction: None) \
        -> None:
    mock_get_exchange_rate_prediction.return_value = 0.95
    assert main.cryptocurrency_action(1.0) == "Do nothing"
