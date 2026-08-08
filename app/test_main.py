import unittest
from unittest.mock import patch
from typing import Any
from .main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(
            self, mock_get_exchange_rate_prediction: Any
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 110
        self.assertEqual(cryptocurrency_action(100), "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(
            self, mock_get_exchange_rate_prediction: Any
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 90
        self.assertEqual(
            cryptocurrency_action(100),
            "Sell all your cryptocurrency"
        )

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_high(
            self, mock_get_exchange_rate_prediction: Any
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 104
        self.assertEqual(cryptocurrency_action(100), "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_low(
            self, mock_get_exchange_rate_prediction: Any
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 96
        self.assertEqual(cryptocurrency_action(100), "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_boundary_buy(
            self, mock_get_exchange_rate_prediction: Any
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 105
        self.assertEqual(cryptocurrency_action(100), "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_boundary_sell(
            self, mock_get_exchange_rate_prediction: Any
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 95
        self.assertEqual(cryptocurrency_action(100), "Do nothing")


if __name__ == "__main__":
    unittest.main()
