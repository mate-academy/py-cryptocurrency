from unittest import mock
from app.main import cryptocurrency_action


def test_func_cryptocurrency_action_higher():
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_func:
        mock_func.return_value = 115
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_func_cryptocurrency_action_lower():
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_func:
        mock_func.return_value = 75
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_func_cryptocurrency_action_difference_105():
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_func:
        mock_func.return_value = 105
        assert cryptocurrency_action(100) == "Do nothing"


def test_func_cryptocurrency_action_difference_95():
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_func:
        mock_func.return_value = 95
        assert cryptocurrency_action(100) == "Do nothing"
