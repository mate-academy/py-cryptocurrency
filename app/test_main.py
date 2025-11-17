from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_get_prediction):
    current = 100
    mock_get_prediction.return_value = 106
    assert cryptocurrency_action(current) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all(mock_get_prediction):
    current = 100
    mock_get_prediction.return_value = 94
    assert cryptocurrency_action(current) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_small_difference(mock_get_prediction):
    current = 100
    mock_get_prediction.return_value = 103
    assert cryptocurrency_action(current) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_upper(mock_get_prediction):
    current = 100
    mock_get_prediction.return_value = 105
    assert cryptocurrency_action(current) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_lower(mock_get_prediction):
    current = 100
    mock_get_prediction.return_value = 95  #
    assert cryptocurrency_action(current) == "Do nothing"
