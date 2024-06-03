import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):
    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(self, mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 1.06

        current_rate = 1.0
        result = cryptocurrency_action(current_rate)

        self.assertEqual(result, "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(self, mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 0.94

        current_rate = 1.0
        result = cryptocurrency_action(current_rate)

        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(self, mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 1.02

        current_rate = 1.0
        result = cryptocurrency_action(current_rate)

        self.assertEqual(result, "Do nothing")


if __name__ == "__main__":
    unittest.main()
