from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_prediction):
    mock_prediction.return_value = 105.1
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_prediction):
    mock_prediction.return_value = 94.9
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_prediction):
    mock_prediction.return_value = 102
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_exactly_5_percent_increase(mock_prediction):
    mock_prediction.return_value = 105.0
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_exactly_5_percent_decrease(mock_prediction):
    mock_prediction.return_value = 95.0
    assert cryptocurrency_action(100) == "Do nothing"
