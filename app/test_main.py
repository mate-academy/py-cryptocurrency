import unittest

from unittest.mock import patch, MagicMock

from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):
    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: MagicMock
    ) -> None:
        current_rate = 1.0
        mock_get_exchange_rate_prediction.return_value = 1.10
        action = cryptocurrency_action(current_rate)
        self.assertEqual(action, "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: MagicMock
    ) -> None:
        current_rate = 1.0
        mock_get_exchange_rate_prediction.return_value = 0.9
        action = cryptocurrency_action(current_rate)
        self.assertEqual(action, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(
            self,
            mock_get_exchange_rate_prediction: MagicMock
    ) -> None:
        current_rate = 1.0
        mock_get_exchange_rate_prediction.return_value = 1.02
        action = cryptocurrency_action(current_rate)
        self.assertEqual(action, "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_rate_105_percent_do_nothing(
            self,
            mock_get_exchange_rate_prediction: MagicMock
    ) -> None:
        current_rate = 1.0
        mock_get_exchange_rate_prediction.return_value = 1.05
        action = cryptocurrency_action(current_rate)
        self.assertEqual(action, "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_rate_95_percent_do_nothing(
            self,
            mock_get_exchange_rate_prediction: MagicMock
    ) -> None:
        current_rate = 1.0
        mock_get_exchange_rate_prediction.return_value = 0.95
        action = cryptocurrency_action(current_rate)
        self.assertEqual(action, "Do nothing")
