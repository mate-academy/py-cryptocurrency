import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action, get_exchange_rate_prediction


class TestCryptocurrencyAction(unittest.TestCase):
    @patch('app.main.get_exchange_rate_prediction')
    def test_buy_more_cryptocurrency(self, mock_get_exchange_rate_prediction):
        # Mock the get_exchange_rate_prediction function to return a value more than 5% higher
        mock_get_exchange_rate_prediction.return_value = 1.06

        result = cryptocurrency_action(100)  # Assuming the current rate is 100
        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch('app.main.get_exchange_rate_prediction')
    def test_sell_all_cryptocurrency(self, mock_get_exchange_rate_prediction):
        # Mock the get_exchange_rate_prediction function to return a value more than 5% lower
        mock_get_exchange_rate_prediction.return_value = 0.94

        result = cryptocurrency_action(100)  # Assuming the current rate is 100
        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch('app.main.get_exchange_rate_prediction')
    def test_do_nothing(self, mock_get_exchange_rate_prediction):
        # Mock the get_exchange_rate_prediction function to return a value within 5%
        mock_get_exchange_rate_prediction.return_value = 1.03

        result = cryptocurrency_action(100)  # Assuming the current rate is 100
        self.assertEqual(result, "Sell all your cryptocurrency")


if __name__ == '__main__':
    unittest.main()