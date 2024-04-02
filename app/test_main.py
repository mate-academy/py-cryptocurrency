import unittest
from unittest.mock import patch
from app import main


class TestCryptoCurrencyAction(unittest.TestCase):

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: unittest.mock.Mock) -> None:
        mock_get_exchange_rate_prediction.return_value = 100 * 1.06
        result = main.cryptocurrency_action(100)
        self.assertEqual(result, "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: unittest.mock.Mock) -> None:
        mock_get_exchange_rate_prediction.return_value = 100 * 0.94
        result = main.cryptocurrency_action(100)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_rate_105_percent_do_nothing(
            self,
            mock_get_exchange_rate_prediction: unittest.mock.Mock) -> None:
        mock_get_exchange_rate_prediction.return_value = 100 * 1.05
        result = main.cryptocurrency_action(100)
        self.assertEqual(result, "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_rate_95_percent_do_nothing(
            self,
            mock_get_exchange_rate_prediction: unittest.mock.Mock) -> None:
        mock_get_exchange_rate_prediction.return_value = 100 * 0.95
        result = main.cryptocurrency_action(100)
        self.assertEqual(result, "Do nothing")
