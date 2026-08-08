import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action
from typing import Union


class TestCryptocurrencyAction(unittest.TestCase):

    @patch("app.main.get_exchange_rate_prediction")
    def test_get_exchange_rate_prediction(
            self,
            mock_exchange_rate: Union[int, float],
    ) -> None:
        mock_exchange_rate.return_value = 1.07
        self.assertEqual(
            cryptocurrency_action(1),
            "Buy more cryptocurrency"
        )

        mock_exchange_rate.return_value = 1.05
        self.assertEqual(
            cryptocurrency_action(1),
            "Do nothing"
        )

        mock_exchange_rate.return_value = 0.95
        self.assertEqual(
            cryptocurrency_action(1),
            "Do nothing"
        )

        mock_exchange_rate.return_value = 0.9
        self.assertEqual(
            cryptocurrency_action(1),
            "Sell all your cryptocurrency")
