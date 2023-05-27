import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action


class CryptocurrencyActionTestCase(unittest.TestCase):
    @patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(self,
                                   mock_get_exchange_rate_prediction: None
                                   ) -> None:
        mock_get_exchange_rate_prediction.return_value = 12.1
        self.assertEqual(cryptocurrency_action(7),
                         "Buy more cryptocurrency")
        mock_get_exchange_rate_prediction.return_value = 1.99
        self.assertEqual(cryptocurrency_action(7),
                         "Sell all your cryptocurrency")
        mock_get_exchange_rate_prediction.return_value = 7
        self.assertEqual(cryptocurrency_action(7),
                         "Do nothing")
