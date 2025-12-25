import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):
    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(self,
                                     mock_get_exchange_rate: str) -> None:
        current_rate = 100
        mock_get_exchange_rate.return_value = current_rate * 1.06
        self.assertEqual(cryptocurrency_action(current_rate),
                         "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(self,
                                     mock_get_exchange_rate: str) -> None:
        current_rate = 100
        mock_get_exchange_rate.return_value = current_rate * 0.94
        self.assertEqual(cryptocurrency_action(current_rate),
                         "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(self,
                        mock_get_exchange_rate: str) -> None:
        current_rate = 100
        mock_get_exchange_rate.return_value = current_rate * 0.97
        self.assertEqual(cryptocurrency_action(current_rate),
                         "Do nothing")

        mock_get_exchange_rate.return_value = current_rate * 1.04
        self.assertEqual(cryptocurrency_action(current_rate), "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_exact_t(self, mock_get_exchange_rate: str) -> None:
        current_rate = 100
        mock_get_exchange_rate.return_value = current_rate * 1.05
        self.assertEqual(cryptocurrency_action(current_rate),
                         "Do nothing")

        mock_get_exchange_rate.return_value = current_rate * 0.95
        self.assertEqual(cryptocurrency_action(current_rate),
                         "Do nothing")
