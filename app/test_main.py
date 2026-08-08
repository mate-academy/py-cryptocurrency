import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):
    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(
            self, mock_get_exchange_rate_prediction: [int, float]) -> None:
        current_rate = 100.0
        predicted_rate = 106.0
        mock_get_exchange_rate_prediction.return_value = predicted_rate
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurency(
            self, mock_get_exchange_rate_prediction: [int, float]) -> None:
        current_rate = 100.0
        predicted_rate = 94.0
        mock_get_exchange_rate_prediction.return_value = predicted_rate
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(
            self, mock_get_exchange_rate_prediction: [int, float]) -> None:
        current_rate = 100.0
        predicted_rate_higher = 105.0
        mock_get_exchange_rate_prediction.return_value = predicted_rate_higher
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Do nothing")
        predicted_rate_lower = 95.0
        mock_get_exchange_rate_prediction.return_value = predicted_rate_lower
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Do nothing")


if __name__ == "__main__":
    unittest.main()
