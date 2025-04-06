import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(self, mock_prediction: float) -> None:
        current_rate = 100
        mock_prediction.return_value = 105.01  # Więcej niż 5% wyższy
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(self, mock_prediction: float) -> None:
        current_rate = 100
        mock_prediction.return_value = 94.99  # Więcej niż 5% niższy
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(self, mock_prediction: float) -> None:
        current_rate = 100
        mock_prediction.return_value = 103  # W zakresie 5%
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Do nothing")


if __name__ == "__main__":
    unittest.main()
