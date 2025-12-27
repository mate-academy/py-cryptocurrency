import unittest
from unittest.mock import patch

from app.main import cryptocurrency_action


class TestMain(unittest.TestCase):
    @patch("app.main.get_exchange_rate_prediction")
    def test_close_to_buy(self, mock_exchange_rate_prediction: int) -> None:
        mock_exchange_rate_prediction.return_value = 5.25
        self.assertEqual(cryptocurrency_action(5), "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_close_to_sell(self, mock_exchange_rate_prediction: int) -> None:
        mock_exchange_rate_prediction.return_value = 4.75
        self.assertEqual(cryptocurrency_action(5), "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_action_buy(self, mock_exchange_rate_prediction: int) -> None:
        mock_exchange_rate_prediction.return_value = 6
        self.assertEqual(cryptocurrency_action(5), "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_action_sell(self, mock_exchange_rate_prediction: int) -> None:
        mock_exchange_rate_prediction.return_value = 1
        self.assertEqual(
            cryptocurrency_action(5),
            "Sell all your cryptocurrency")
