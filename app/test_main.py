import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action
from typing import Callable


class TestCryptocurrencyAction(unittest.TestCase):

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more(self, mock_exchange_rate: Callable) -> None:
        mock_exchange_rate.return_value = 5.26
        assert cryptocurrency_action(5) == "Buy more cryptocurrency"

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all(self, mock_exchange_rate: Callable) -> None:
        mock_exchange_rate.return_value = 4.74
        assert cryptocurrency_action(5) == "Sell all your cryptocurrency"

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(self, mock_exchange_rate: Callable) -> None:
        mock_exchange_rate.return_value = 5.25
        assert cryptocurrency_action(5) == "Do nothing"
        mock_exchange_rate.return_value = 4.75
        assert cryptocurrency_action(5) == "Do nothing"
