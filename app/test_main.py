from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy(mock_get_exchange_rate_prediction: object):
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 106
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell(mock_get_exchange_rate_prediction: object):
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 94
    assert cryptocurrency_action(current_rate) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(mock_get_exchange_rate_prediction):
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(current_rate) == "Do nothing"

    mock_get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(current_rate) == "Do nothing"


