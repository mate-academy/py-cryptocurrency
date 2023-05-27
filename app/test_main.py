import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action


class CryptocurrencyActionTestCase(unittest.TestCase):
    @patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(self,
                                   mock_get_exchange_rate_prediction: None
                                   ) -> None:
        mock_get_exchange_rate_prediction.return_value = 105.1
        self.assertEqual(cryptocurrency_action(100),
                         "Buy more cryptocurrency")
        mock_get_exchange_rate_prediction.return_value = 94.9
        self.assertEqual(cryptocurrency_action(100),
                         "Sell all your cryptocurrency")
        mock_get_exchange_rate_prediction.return_value = 101
        self.assertEqual(cryptocurrency_action(100),
                         "Do nothing")
