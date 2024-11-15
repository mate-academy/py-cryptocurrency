import unittest
from unittest.mock import patch, MagicMock

from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: MagicMock) -> None:
        mock_get_exchange_rate_prediction.return_value = 105.1
        current_rate = 100
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Buy more cryptocurrency")


    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: MagicMock) -> None:
        mock_get_exchange_rate_prediction.return_value = 94.9
        current_rate = 100
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(
            self,
            mock_get_exchange_rate_prediction: MagicMock) -> None:
        mock_get_exchange_rate_prediction.return_value = 102.0
        current_rate = 100
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Do nothing")

        mock_get_exchange_rate_prediction.return_value = 105.0
        current_rate = 100
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Do nothing")

        mock_get_exchange_rate_prediction.return_value = 95.0
        current_rate = 100
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Do nothing")