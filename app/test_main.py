import pytest
<<<<<<< HEAD
from app.main import cryptocurrency_action
from unittest.mock import patch


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 94
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"

@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 100
    result = cryptocurrency_action(106)
    assert result == "Buy more cryptocurrency"

@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 100
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
=======
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestClass:
    @patch("app.main.get_exchange_rate_prediction")
    def test_first_func(mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 110
        result = cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"
>>>>>>> da58aecf37135280f0d460e45ab54d53f9212d7f
