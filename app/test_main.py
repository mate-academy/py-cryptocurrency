import unittest
from unittest.mock import patch, MagicMock

from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more(self, mock_prediction: MagicMock) -> None:
        current_rate = 100.0
        predicted_rate = 105.01
        mock_prediction.return_value = predicted_rate
        action = cryptocurrency_action(current_rate)
        self.assertEqual(action, "Buy more cryptocurrency")
        mock_prediction.assert_called_once()

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all(self, mock_prediction: MagicMock) -> None:
        current_rate = 100.0
        predicted_rate = 94.99
        mock_prediction.return_value = predicted_rate
        action = cryptocurrency_action(current_rate)
        self.assertEqual(action, "Sell all your cryptocurrency")
        mock_prediction.assert_called_once()

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_higher_within_threshold(
            self, mock_prediction: MagicMock) -> None:
        current_rate = 100.0
        predicted_rate = 105.00
        mock_prediction.return_value = predicted_rate
        action = cryptocurrency_action(current_rate)
        self.assertEqual(action, "Do nothing")
        mock_prediction.assert_called_once()

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_lower_within_threshold(
            self, mock_prediction: MagicMock) -> None:
        current_rate = 100.0
        predicted_rate = 95.00
        mock_prediction.return_value = predicted_rate
        action = cryptocurrency_action(current_rate)
        self.assertEqual(action, "Do nothing")
        mock_prediction.assert_called_once()

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_same_rate(self, mock_prediction: MagicMock) -> None:
        current_rate = 100.0
        predicted_rate = 100.0
        mock_prediction.return_value = predicted_rate
        action = cryptocurrency_action(current_rate)
        self.assertEqual(action, "Do nothing")
        mock_prediction.assert_called_once()
