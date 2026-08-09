import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):
    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(
            self, mock_get_exchange_rate_prediction: callable
    ) -> None:
        current_rate = 100
        mock_get_exchange_rate_prediction.return_value = 106
        self.assertEqual(cryptocurrency_action(current_rate),
                         "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(
            self, mock_get_exchange_rate_prediction: callable
    ) -> None:
        current_rate = 100
        mock_get_exchange_rate_prediction.return_value = 94
        self.assertEqual(cryptocurrency_action(current_rate),
                         "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_rate_95_percent_do_nothing(
            self, mock_get_exchange_rate_prediction: callable) -> None:
        mock_get_exchange_rate_prediction.return_value = 95
        current_rate = 100
        self.assertEqual(cryptocurrency_action(current_rate),
                         "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_rate_105_percent_do_nothing(
            self, mock_get_exchange_rate_prediction: callable) -> None:
        mock_get_exchange_rate_prediction.return_value = 105
        current_rate = 100
        self.assertEqual(cryptocurrency_action(current_rate),
                         "Do nothing")
